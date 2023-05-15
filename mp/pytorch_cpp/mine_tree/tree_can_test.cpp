#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<map>
#include<vector>
#include<tuple>
#include<deque>
#include<utility>
using namespace std;
class tree_node{
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
};
bool bin_pred(string s1, string s2){
    istringstream ss1(s1), ss2(s2);
    string tmp1, tmp2;
    int l1, l2;
    while(ss1 >> tmp1 && ss2 >> tmp2){
        if(tmp1.compare("$") == 0){
            return false;
        }
        if(tmp2.compare("$") == 0)
            return true;
        if(tmp1.compare(tmp2) == 0){
            continue;
        }
        l1 = stoi(tmp1);
        l2 = stoi(tmp2);
        return l1 < l2;
    }
    if(ss2)
        return false;
    if(ss1)
        return true;
}
string get_can_lab_tree(const vector<tree_node*> &tree, int root=0){
    string s, child_label;
    stringstream ss;
    ss << tree[root]->label;
    if (tree[root]->children.size() != 0){
        vector<string> child_labels;
        for(vector<pair<int, int>>::iterator it=tree[root]->children.begin(); it!=tree[root]->children.end(); it++){
            child_label = get_can_lab_tree(tree, it->first);
            child_label.insert(0, 1, ' ');
            child_label.insert(0, to_string(it->second));
            child_labels.push_back(child_label);
        }
        sort(child_labels.begin(), child_labels.end(), bin_pred);
        for(vector<string>::iterator it=child_labels.begin(); it!=child_labels.end(); it++){
            ss << " " << *it;
        }
    }
    ss << " $";
    getline(ss, s);
    return s;
}
int main(int argc, char* argv[]){
    vector<tree_node*> tree;
    tree.push_back(new tree_node(1, 0));
    tree.push_back(new tree_node(2, 1));
    tree.push_back(new tree_node(3, 2));
    tree.push_back(new tree_node(4, 3));
    tree.push_back(new tree_node(5, 4));
    tree.push_back(new tree_node(6, 5));
    tree[0]->insert_child(1, 7);
    tree[0]->insert_child(2, 7);
    tree[1]->insert_child(3, 7);
    tree[1]->insert_child(4, 7);
    tree[4]->insert_child(5, 7);
    string s = get_can_lab_tree(tree);
    cout << s;
    return 0;
}
