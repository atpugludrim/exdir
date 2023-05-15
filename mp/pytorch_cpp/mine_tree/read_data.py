r"""This code generates MPTrees for ogbg datasets. The code right now is
specific for molbace (it deals with edge attribute issues specific to it).
It can be adapted to others.
"""
import time
import torch

# import pygread
# import pybind_test
import pygcanl

from ogb.graphproppred import PygGraphPropPredDataset
from torch_geometric.data import Data


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
            x=torch.tensor([node_label_map[n.item()] for n in d.x[:, 0]]),
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


# -------------------  GET RAW DATASET  -----------------------
def get_raw_dataset(dataset_name):
    if dataset_name in ["ogbg-molhiv", "ogbg-molbbbp", "ogbg-molbace"]:
        dataset = PygGraphPropPredDataset(name=dataset_name)
    return dataset


# ------------------  </GET RAW DATASET>  ---------------------


def main():
    dataset_name = "ogbg-molbace"
    proc_data = preprocess_dataset(get_raw_dataset(dataset_name))
    # for i in range(1):#len(proc_data)):
    #    pygread.read_graph(proc_data[i].x, proc_data[i].edge_index, proc_data[i].edge_attr, proc_data[i].original_x, proc_data[i].y)
    # ret=torchcanonl.canonical_labelizer(proc_data[i].x, proc_data[i].edge_index, proc_data[i].original_x, proc_data[i].edge_attr, proc_data[i].original_edge_attr, proc_data[i].y)
    # ret = pybind_test.canonical_labelizer(proc_data)
    t1 = time.perf_counter()
    ret = pygcanl.canonical(proc_data, 2)
    t2 = time.perf_counter()
    print(f"ret {ret} {t2-t1}s")
    print(len(proc_data))
    print(len(ret))
    print(max(list(map(len, ret))))


if __name__ == "__main__":
    main()
