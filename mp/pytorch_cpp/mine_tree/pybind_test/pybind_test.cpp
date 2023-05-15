#include<torch/extension.h>
#include<iostream>
#include<boost/graph/adjacency_list.hpp>
#include<utility>
#include<vector>
#include<map>
#include<string>
/*py::str canonical_labelizer(torch::Tensor x, torch::Tensor edge_index, torch::Tensor original_x,
        torch::Tensor edge_attr, torch::Tensor original_edge_attr, torch::Tensor y){
        */
py::list canonical_labelizer(py::list list){
    for(auto item : list){
        py::object x = item.attr("x");
        py::int_ size = x.attr("size")(0);
        int size_ = size;
        std::cout << size_;
        std::cout<<"\nPrinting x of len "<<size<<"\n";
        std::cout<<x[py::cast(2)].attr("item")()<<";;;";
        for(auto i : x){
            std::cout << i.attr("item")() <<" ";
        }
        std::cout << std::endl;
        // std::cout << x;
        // std::cout << item;
    }
    std::vector<std::vector<std::string>> v_;
    std::vector<std::string> v;
    v.push_back("this");
    v.push_back("bitch");
    v_.push_back(v);
    return py::cast(v_);
}
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m){
    m.def("canonical_labelizer", &canonical_labelizer, py::return_value_policy::take_ownership,"Find canonical label of all the trees of the graph");
}
