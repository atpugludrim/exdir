import os
import torch
import pickle
import numpy as np
from torch.utils.data import DataLoader, Dataset
from mine_trees import preprocess_dataset, get_raw_dataset, select_dataset
from mine_trees import remove_invalid_trees, get_classwise_transactions
from mine_trees import generate_trees, get_classwise_frequent


class MyTrainDataset(Dataset):
    def __init__(this, trees_classwise, class_, perc=80):
        this.trees_classwise = trees_classwise
        this.perc = perc
        this.class_ = class_
        this.init_pairs()

    def init_pairs(this):
        xs = []
        ys = []
        for tree in this.trees_classwise[this.class_]:
            xs.append(tree)
        this.w2i, this.i2w = calculate_w2i_and_i2w(xs)
        xx = [
            list(map(lambda el: this.w2i[el], list(str(x)))) for x in xs
        ]  # convert to seq of ints
        xs, ys = get_nxt_wrd_pairs(xx)
        permutation = np.random.RandomState(seed=0).permutation(len(xs))
        train_len = int(np.ceil(len(xs) * this.perc / 100.0))
        train_idx = permutation[:train_len]
        test_idx = permutation[train_len:]
        train_xs, train_ys = [], []
        test_xs, test_ys = [], []
        for i in train_idx:
            train_xs.append(xs[i])
            train_ys.append(ys[i])
        for i in test_idx:
            test_xs.append(xs[i])
            test_ys.append(ys[i])
        this.train_xs = train_xs
        this.test_xs = test_xs
        this.train_ys = train_ys
        this.test_ys = test_ys

    def __getitem__(this, idx):
        return torch.tensor(this.train_xs[idx]), torch.tensor(this.train_ys[idx])

    def __len__(this):
        return len(this.train_xs)


class MyValDataset(Dataset):
    def __init__(this, valx, valy):
        this.valx = valx
        this.valy = valy

    def __getitem__(this, i):
        return torch.tensor(this.valx[i]), torch.tensor(this.valy[i])

    def __len__(this):
        return len(this.valx)


def pad_collate_fn(batch):
    x, y = zip(*batch)  # need to split and convert to integers and make w2i and i2w
    lens = [len(el) for el in x]
    x = torch.nn.utils.rnn.pad_sequence(x, batch_first=True, padding_value=0)
    return x, torch.tensor(y), lens


def calculate_w2i_and_i2w(vocab):
    w2i = {}

    def inf_ctr():
        ctr = 1
        while True:
            yield ctr
            ctr += 1

    ctr = inf_ctr()
    for string in vocab:
        for token in list(str(string)):
            itoken = w2i.get(token, None)
            w2i[token] = next(ctr) if itoken is None else itoken
    i2w = {v: k for k, v in w2i.items()}
    return w2i, i2w


def get_nxt_wrd_pairs(xx):
    xs, ys = [], []
    for x in xx:
        for i in range(1, len(x) - 1):
            xs.append(x[:i])
            ys.append(x[i])
    return xs, ys


def collapse_patterns_classwise(patterns, ints):
    trees = {}
    ints_inverse = {v: k for k, v in ints.items()}
    for class_, patterns_ in patterns.items():
        trees[class_] = set()
        for pattern in patterns_.keys():
            [trees[class_].add(ints_inverse[tid]) for tid in pattern]
    return trees


def get_data(dataset_name, freq_thresholds):
    if os.path.isfile("cache.pkl"):
        with open("cache.pkl", "rb") as f:
            data = pickle.load(f)
        canlabs = data["canlabs"]
        f1 = data["f1"]
        f2 = data["f2"]
        f3 = data["f3"]
        f4 = data["f4"]
    else:
        train_data, test_data = select_dataset(
            preprocess_dataset(get_raw_dataset(dataset_name))
        )
        canlabs, f1, f2, f3, f4 = remove_invalid_trees(*generate_trees(train_data))
        with open("cache.pkl", "wb") as f:
            pickle.dump(
                {
                    "canlabs": canlabs,
                    "f1": f1,
                    "f2": f2,
                    "f3": f3,
                    "f4": f4,
                    "test_data": test_data,
                },
                f,
            )
    transactions, ints = get_classwise_transactions(canlabs, f1, f3)
    patterns = get_classwise_frequent(transactions, freq_thresholds)
    trees_classwise = collapse_patterns_classwise(patterns, ints)
    class0_dataset = MyTrainDataset(trees_classwise, 0)
    class1_dataset = MyTrainDataset(trees_classwise, 1)
    test_x0, test_y0 = class0_dataset.test_xs, class0_dataset.test_ys
    test_x1, test_y1 = class1_dataset.test_xs, class1_dataset.test_ys
    val0_dataset = MyValDataset(test_x0, test_y0)
    val1_dataset = MyValDataset(test_x1, test_y1)
    dataloader0 = DataLoader(
        class0_dataset, batch_size=32, shuffle=True, collate_fn=pad_collate_fn
    )
    dataloader1 = DataLoader(
        class1_dataset, batch_size=32, shuffle=True, collate_fn=pad_collate_fn
    )
    vdataloader0 = DataLoader(val0_dataset, batch_size=32, collate_fn=pad_collate_fn)
    vdataloader1 = DataLoader(val1_dataset, batch_size=32, collate_fn=pad_collate_fn)
    return dataloader0, dataloader1, vdataloader0, vdataloader1
