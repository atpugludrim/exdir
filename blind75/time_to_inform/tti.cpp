#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<utility>
#include<climits>
using namespace std;
// enum graph_color {WHITE, GRAY, BLACK};
// since everybody has just one manager, it's basically a tree
// and this is not required
class graph{
    private:
        int nodeId, informTime;
    public:
        vector<graph*> adj;
        // graph_color color;
        graph(int nodeId, int informTime){
            this->nodeId = nodeId;
            this->informTime = informTime;
            // color = WHITE;
        }
        void insert_neighbor(graph *nb_ptr){
            adj.push_back(nb_ptr);
        }
        int getId(void){
            return nodeId;
        }
        int getInformTime(void){
            return informTime;
        }
};
void traverse_graph(graph*);
int numOfMinutes(int, int, vector<int>&, vector<int>&);
int equalPartition(vector<int>&, int, vector<int>&, vector<int>&);
int dfs_util(graph*, int, int);
int main(int argc, char *argv[]){
    if(argc < 3){
        cout<<"usage: "<<argv[0]<<" <n> <headID>\n";
        return 0;
    }
    int n = atoi(argv[1]);
    int headID = atoi(argv[2]);
    vector<int> manager;
    for(int i = 0; i < n; i++){
        int m;
        cin>>m;
        manager.push_back(m);
    }
    vector<int> informTime;
    for(int i = 0; i < n; i++){
        int it;
        cin>>it;
        informTime.push_back(it);
    }
    int nom = numOfMinutes(n, headID, manager, informTime);
    cout<<nom<<endl;
}
int equalPartition(vector<int>& arr, int piv, vector<int>& args, vector<int>& inft){
    int i = -1;
    int j = arr.size();
    int n = j;
    //cout<<piv<<"\n";
    while(i<j && i < n && j >= 0){
        while(arr[++i]!=piv){
            if(i==(n-1)){
                i++;
                break;
            }
        }
        while(arr[--j]==piv){
            if(j==0){
                j--;
                break;
            }
        }
        if(i>=j)
            break;
        iter_swap(arr.begin()+i,arr.begin()+j);
        iter_swap(args.begin()+i,args.begin()+j);
        iter_swap(inft.begin()+i,inft.begin()+j);
    }
    return i;
}
int numOfMinutes(int n, int headId, vector<int>& manager, vector<int>& informTime){
    // step 1: create graph
    if(manager.size() <= 1){
        return 0;
    }
    int curr_mgr_id;
    vector<int> args;
    graph head_node = graph(headId, informTime[headId]), *curr_node;
    queue<graph*> q;
    q.push(&head_node);
    for(int i = 0; i < n; i++){
        args.push_back(i);
    }
    while(!q.empty()){
        curr_node = q.front();
        curr_mgr_id = curr_node->getId();
        q.pop();
        int p = equalPartition(manager, curr_mgr_id, args, informTime);
        for(int i = p; i < n; i++){
            graph *newnode = new graph(args[i],informTime[i]);
            curr_node->insert_neighbor(newnode);
            q.push(newnode);
        }
    }
    //traverse_graph(&head_node);

    // step 2: do dfs in extended manner, returning things
    return dfs_util(&head_node, 0, INT_MIN);
}
int dfs_util(graph *root, int path_acc, int max){
    if(root->adj.size() == 0){
        if(max < path_acc + root->getInformTime()){
            max = path_acc + root->getInformTime();
        }
        return max;
    }
    else{
        for(vector<graph*>::iterator it = root->adj.begin(); it!=root->adj.end(); it++){
            int retval = dfs_util(*it, path_acc + root->getInformTime(), max);
            if(retval > max){
                max = retval;
            }
        }
        return max;
    }
}
void traverse_graph(graph *root){
    queue<pair<graph*,int>> q;
    pair<graph*, int> item;
    q.push(make_pair(root,0));
    graph *curr;
    int level;
    while(!q.empty()){
        item = q.front();
        curr = item.first;
        level = item.second;
        for(int i=0; i < level; i++){
            cout<<" ";
        }
        cout<<curr->getId()<<" takes time: "<<curr->getInformTime()<<"\n";
        q.pop();
        for(vector<graph*>::iterator it=curr->adj.begin(); it!=curr->adj.end(); it++){
            q.push(make_pair(*it,level+1));
        }
    }
}
