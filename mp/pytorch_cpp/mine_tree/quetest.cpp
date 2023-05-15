#include<iostream>
#include<deque>
#include<utility>
#include<tuple>
using namespace std;
/*class tree_node{
    public:
        int label, idx;
        vector<pair<int, int>> children;
        tree_node(const int &lab, const int &idx_){
            label = lab;
            idx = idx_;
        }
        void insert_child(const int &child_idx, const int &edge_label){
            children.push_back(make_pair(child_idx, edge_label));
        }
};*/
int main(int argc, char* argv[]){
    deque<tuple<int, int, int>> Q;
    Q.push_back(make_tuple(3, 2, 4));
    int a, b, c;
    tie(a,b,c) = Q.front();
    cout<<a<<" "<<b<<" "<<c<<"\n";
    return 0;
}
