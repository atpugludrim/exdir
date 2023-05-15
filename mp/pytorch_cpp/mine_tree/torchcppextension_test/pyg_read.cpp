#include<torch/extension.h>
#include<boost/graph/adjacency_list.hpp>
#include<iostream>
#include<vector>
#include<string>
torch::Tensor read_graph(torch::Tensor x, torch::Tensor edge_index, torch::Tensor edge_attr, torch::Tensor original_x, torch::Tensor y){
    // everything but x and edge_attr is 2D.
    struct status_t { typedef boost::vertex_property_tag kind;};
    struct edge_prop_t { typedef boost:: edge_property_tag kind;};
    typedef boost::property<status_t, int> VertexProperty;
    typedef boost::property<edge_prop_t, int> EdgeProperty;
    typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::directedS, VertexProperty, EdgeProperty> Graph;
    Graph g(x.size(0));
    auto ei_a = edge_index.accessor<long, 2>();
    boost::add_edge(ei_a[0][0], ei_a[1][0], g);
    //boost::property_map<Graph, EdgeProperty>::type edgeprop = get(edge_prop_t(), G);
    auto y_a = y.accessor<long, 2>();
    return y;
}
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m){
    m.def("read_graph", &read_graph, "read_graph");
}
