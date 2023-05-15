r"""This code generates MPTrees for ogbg datasets. The code right now is
specific for molbace (it deals with edge attribute issues specific to it).
It can be adapted to others.
"""
import torch
import numpy as np
import networkx as nx
from multiprocessing import Pool, Manager, Lock
from itertools import zip_longest

from ogb.graphproppred import PygGraphPropPredDataset
from torch_geometric.data import Data
from torch_geometric.utils import to_networkx

import pyfpgrowth


# ---------------  PROCESS DATASET (LABELS)  ------------------
def get_label_maps(dataset):
    edge_attrs = set()
    for d in dataset:
        edge_attr = d.edge_attr
        [
            edge_attrs.add(tuple(edge_attr[ea, :].tolist()))
            for ea in range(edge_attr.shape[0])
        ]
    node_labels = set()
    for d in dataset:
        node_label = d.x[:, 0]
        [node_labels.add(n.item()) for n in node_label]
    node_label_map = {n: idx for idx, n in enumerate(node_labels)}
    edge_label_map = {edge_config: idx for idx, edge_config in enumerate(edge_attrs)}
    return node_label_map, edge_label_map


def process_labels(dataset, node_label_map, edge_label_map):
    dataset_ = []
    for d in dataset:
        data = Data(
            x=d.x[:, 0],
            original_x=d.x,
            edge_index=d.edge_index,
            y=d.y,
            original_edge_attr=d.edge_attr,
            edge_attr=torch.tensor(
                [
                    edge_label_map[tuple(d.edge_attr[ea, :].tolist())]
                    for ea in range(d.edge_attr.shape[0])
                ],
                dtype=torch.long,
            ),
        )
        dataset_.append(data)
    return dataset_


def preprocess_dataset(dataset):
    node_label_map, edge_label_map = get_label_maps(dataset)
    label_processed_dataset = process_labels(
        dataset,
        node_label_map,
        edge_label_map,
    )
    return label_processed_dataset


# ------------  </PREPROCESS DATASET (LABELS)>  ---------------


# ----------------  SELECT SUBSET OF DATA  --------------------
def permute(label_processed_dataset, seed=0):
    perm = np.random.RandomState(seed=seed).permutation(len(label_processed_dataset))
    shuffled = []
    for i in perm:
        shuffled.append(label_processed_dataset[i])
    return shuffled


def select_dataset(dataset, perc_train=80):
    permuted_dataset = permute(dataset)
    train_upto = int(np.ceil(len(permuted_dataset) * perc_train / 100.0))
    train_data, test_data = dataset[:train_upto], dataset[train_upto:]
    return train_data, test_data


# ---------------  </SELECT SUBSET OF DATA>  ------------------


# -------------------  GET RAW DATASET  -----------------------
def get_raw_dataset(dataset_name):
    if dataset_name in ["ogbg-molhiv", "ogbg-molbbbp", "ogbg-molbace"]:
        dataset = PygGraphPropPredDataset(name=dataset_name)
    return dataset


# ------------------  </GET RAW DATASET>  ---------------------


# --------------------  MPTREE MINING  ------------------------
def get_MPTree(Graph, root_node, hops):
    assert hops < 5
    G = Graph.to_undirected()
    MPTree = nx.DiGraph()

    def inf_counter():
        ctr = 0
        while True:
            yield ctr
            ctr += 1

    ctr = inf_counter()
    start = root_node
    hop = 0
    Q = [(start, next(ctr), hop)]
    MPTree.add_node(
        Q[0][1],
        nodeorigid=start,
        label=G.nodes[start]["label"],
        original_x=G.nodes[start]["original_x"],
    )
    while hop < hops and len(Q) > 0:
        top, topid, hop = Q.pop(0)
        if hop >= hops:
            continue
        neighbors = G.neighbors(top)
        for neighbor, new_id in zip(neighbors, ctr):
            MPTree.add_node(
                new_id,
                nodeorigid=neighbor,
                label=G.nodes[neighbor]["label"],
                original_x=G.nodes[neighbor]["original_x"],
            )
            MPTree.add_edge(
                topid,
                new_id,
                label=G.get_edge_data(top, neighbor)["label"],
                original_edge_attr=G.get_edge_data(top, neighbor)["original_edge_attr"],
            )
            Q.append((neighbor, new_id, hop + 1))
    return MPTree


def get_labels(G):
    for node1, node2, data in G.edges.data():
        label_value = data["edge_attr"]
        G.edges[node1, node2]["label"] = label_value
        G.edges[node2, node1]["label"] = label_value
    for i in range(0, len(G)):
        label_value = G.nodes[i]["x"]
        G.nodes[i]["label"] = label_value
    return G


def get_can_lab_tree(tree, root=0):
    if tree.out_degree(root) == 0:
        return int(f'1{tree.nodes[root]["label"]+2}0')
    child_labels = []
    for child in tree.adj[root]:
        child_label = get_can_lab_tree(tree, child)
        edge_label = tree.get_edge_data(root, child)["label"]
        child_labels.append(int(f"{child_label}{edge_label+2}"))
    child_labels = sorted(child_labels)
    can_lab = int(
        f'1{tree.nodes[root]["label"]+2}{"".join(str(c) for c in child_labels)}0'
    )
    return can_lab


def to_nx(data):
    G = to_networkx(
        data,
        node_attrs=["x", "original_x"],
        edge_attrs=["edge_attr", "original_edge_attr"],
    )
    return G


lock = Lock()
def generate_trees(dataset, n_hops=3):
    num_workers = 2
    batches = [dataset[i::num_workers] for i in range(num_workers)]
    args = zip_longest(batches, [], fillvalue=n_hops)
    m = Manager()
    f1, f2, f3, f4, canlabs = m.dict(), m.dict(), m.dict(), m.dict(), m.dict()
    with Pool(processes=num_workers) as pool:
        pool_iter = [pool.apply_async(generate_trees_, (arg, canlabs, f1, f2, f3, f4)) for arg in args]
        for pool_worker in pool_iter:
            result = pool_worker.get()
    import pdb;pdb.set_trace()


def generate_trees_(args, canlabs, f1, f2, f3, f4):
    dataset, n_hops = args
    for idx, data in enumerate(dataset):
        class_ = data.y.item()
        with lock:
            if class_ not in f3:
                f3[class_] = []
            f3[class_].append(idx)
            f1[idx] = []
        if idx % 50 == 0:
            print(f"Processing: {idx}")
        G = to_nx(data)
        G = get_labels(G)
        for node in G.nodes:
            MPTree = get_MPTree(G, node, n_hops)
            if len(MPTree) <= 1:
                continue
            canlab = get_can_lab_tree(MPTree)
            with lock:
                canlab_count = canlabs.get(canlab, 0)
                canlabs[canlab] = canlab_count + 1
                # populate the functions
                if canlab not in f4:
                    f4[canlab] = {}
                class_count = f4[canlab].get(class_, 0)
                f4[canlab][class_] = class_count + 1
                f1[idx].append(canlab)
                if canlab not in f2:
                    f2[canlab] = []
                f2[canlab].append(idx)


def remove_invalid_trees(canlabs, f1, f2, f3, f4):
    # Sophisticated logic can be written here. Going for simple removal of trees
    # that appear in both classes.
    def invalid_check(cts):
        return len(cts) > 1

    invalid_trees = [tree for tree, cts in f4.items() if invalid_check(cts)]
    f1 = {k: [v for v in vals if v not in invalid_trees] for k, vals in f1.items()}
    f2 = {k: v for k, v in f2.items() if k not in invalid_trees}
    f4 = {k: v for k, v in f4.items() if k not in invalid_trees}
    canlabs = {k: v for k, v in canlabs.items() if k not in invalid_trees}
    return canlabs, f1, f2, f3, f4


def get_classwise_transactions(canlabs, f1, f3):
    ints = {v: k for k, v in enumerate(canlabs)}
    # graph_idxs : list of graph idxs in class_
    # f1 : graph -> trees
    # ints: tree -> int
    # task: convert list of graph_idxs to list of trees to list of ints = transactions
    transactions = {
        class_: [[ints[t] for t in f1[g]] for g in graph_idxs]
        for class_, graph_idxs in f3.items()
    }
    return transactions, ints


def get_classwise_frequent(transactions, thresholds):
    patterns = {}
    for class_ in transactions:
        transactions_ = transactions[class_]
        threshold = thresholds[class_]
        patterns_ = pyfpgrowth.find_frequent_patterns(transactions_, threshold)
        patterns[class_] = patterns_
    return patterns


def main():
    dataset_name = "ogbg-molbace"
    proc_data = preprocess_dataset(get_raw_dataset(dataset_name))
    train_data, test_data = select_dataset(proc_data)
    canlabs, f1, f2, f3, f4 = generate_trees(train_data)
    canlabs, f1, f2, f3, f4 = remove_invalid_trees(canlabs, f1, f2, f3, f4)
    transactions, _ = get_classwise_transactions(canlabs, f1, f3)
    freq_thresholds = {0: 5, 1: 10}
    patterns = get_classwise_frequent(transactions, freq_thresholds)
    print(f"Patterns mined: {patterns}")


if __name__ == "__main__":
    main()
