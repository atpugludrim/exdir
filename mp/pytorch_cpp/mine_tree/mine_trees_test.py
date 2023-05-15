r"""This code generates MPTrees for ogbg datasets. The code right now is
specific for molbace (it deals with edge attribute issues specific to it).
It can be adapted to others.
"""
import time
import torch
import pygcanl
# import networkx as nx
# import matplotlib.pyplot as plt

from ogb.graphproppred import PygGraphPropPredDataset
from torch_geometric.data import Data
from torch_geometric.utils import to_networkx


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


# ----------------  PROCESS CANONICAL LABELS  -----------------
def prettify_canonical_label(label):
    assert isinstance(label, str)
    tokens = label.split()
    label2 = tokens[0]
    ptr = 1
    while ptr < len(tokens):
        if tokens[ptr] == "$":
            label2 += tokens[ptr]
            ptr += 1
        else:
            edge_label = tokens[ptr]
            node_label = tokens[ptr+1]
            ptr += 2
            label2 += f"<{edge_label},{node_label}>"
    return label2


def canonical_label_to_naturals(dataset_labels):
    mapping = {}
    ctr = 0
    for graph_labels in dataset_labels:
        for label in graph_labels:
            if label not in mapping:
                mapping[label] = ctr
                ctr += 1
    return mapping
# --------------  </PROCESS CANONICAL LABELS>  ----------------


# ---------------  COMPUTE FREQUENT PATTERNS  -----------------
def tree_class_ctr(classes, dataset):
    tree_class_count = {}
    for class_,graph in zip(classes,dataset):
        for tree in graph:
            if tree not in tree_class_count:
                tree_class_count[tree]={}
            if class_ not in tree_class_count[tree]:
                tree_class_count[tree][class_] = 0
            tree_class_count[tree][class_] += 1
    return tree_class_count


def get_invalid_trees(tree_class_count):
    trees = []
    for tree,ctr in tree_class_count.items():
        if len(ctr) != 1:
            trees.append(tree)
    return trees
# -------------  </COMPUTE FREQUENT PATTERNS>  ----------------


def main():
    import pickle
    with open('9928.pkl','rb') as f:
        data = pickle.load(f)
    dat = Data(x=data['x'],edge_attr=data['ea'],edge_index=data['ei'],original_x=data['x'],original_edge_attr=data['ea'],y=torch.tensor([[1]]))
    data = [dat]
    ret = pygcanl.canonical(data, 2)
    import pdb;pdb.set_trace()


if __name__ == "__main__":
    main()
