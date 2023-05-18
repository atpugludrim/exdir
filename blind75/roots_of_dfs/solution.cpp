#include<iostream>
#include<vector>
#include<numeric>
#include<map>
#include<algorithm>
using namespace std;
class Solution{
    public:
        vector<int> argsort(const vector<int>& arr){//https://gist.github.com/HViktorTsoi/58eabb4f7c5a303ced400bcfa816f6f5
            vector<int> indices(arr.size());
            iota(indices.begin(), indices.end(), 0);
            sort(indices.begin(), indices.end(),
                    [&arr](const int& left, const int& right) -> bool{
                        return arr[left] < arr[right];
                    }
                );
            return indices;
        }
        vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges){
            // construct adjacency list
            map<int, vector<int>> adjacency_list;
            vector<int> in_degrees(n, 0);
            int u, v;
            for(auto edge:edges){
                u = edge[0];
                v = edge[1];
                if(adjacency_list.count(u) == 0){
                    vector<int> adjacency;
                    adjacency.push_back(v);
                    adjacency_list[u] = adjacency;
                }
                else{
                    adjacency_list[u].push_back(v);
                }
                in_degrees[v] += 1;
            }
            // perform dfs and get dfs trees
            vector<int> visited(n, 0);
            vector<int> has_par(n, 0);
            vector<int> argsorted = argsort(in_degrees);
            int node;
            for(int i=0;i<n;i++){ // <-- assumes node ids are 0,1,...,n-1
                node = argsorted[i];
                if(!visited[node]){
                    dfs(node, adjacency_list, visited, has_par);
                }
            }
            vector<int> result;
            for(int i = 0; i < n; i++){
                if(has_child[i] == 0){
                    result.push_back(i);
                }
            }
            return result;
        }
        void dfs(int node,
                 map<int, vector<int>>& adjacency_list,
                 vector<int>& visited,
                 vector<int>& has_par){
            visited[node] = 1;
            for(auto nbr:adjacency_list[node]){
                if(!visited[nbr]){
                    has_par[nbr] = 1;
                    dfs(nbr, adjacency_list, visited, has_par);
                }
            }
        }
};
int main(int argc, char* argv[]){
    int N, M, u, v;
    vector<vector<int>> edges;
    cin >> N >> M;
    for(int i = 0; i < M; i++){
        cin >> u >> v;
        vector<int> edge;
        edge.push_back(u);
        edge.push_back(v);
        edges.push_back(edge);
    }
    Solution solution = Solution();
    vector<int> result;
    result = solution.findSmallestSetOfVertices(N, edges);
    for(auto v:result){
        cout << v << ' ';
    }
    cout << '\n';
    return 0;
}
