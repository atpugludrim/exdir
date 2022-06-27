#include<iostream>
#include<utility>
#include<vector>
#include<stack>
using namespace std;
int dfs(vector<vector<char>> &grid, const int &start_i, const int &start_j, const int &m, const int &n){
    if(grid[start_i][start_j]!='1'){
        return 0;
    }
    stack<pair<int, int>> s;
    int curr_i, curr_j, next_i, next_j;
    pair<int, int> item;
    s.push(make_pair(start_i, start_j));
    int dx[] = {1,-1,0,0}, dy[] = {0,0,1,-1};
    while(!s.empty()){
        item = s.top();
        s.pop();
        curr_i = item.first;
        curr_j = item.second;
        for(int i = 0; i < 4; i++){
            next_i = curr_i + dy[i];
            next_j = curr_j + dx[i];
            if(0<=next_i && next_i<m && 0<=next_j && next_j<n && grid[next_i][next_j] == '1'){
                s.push(make_pair(next_i, next_j));
            }
        }
        grid[curr_i][curr_j] = 'V';
    }
    return 1;
}
int numIslands(vector<vector<char>> &grid){
    // grid allowed to be modified, I can use it to track visited
    // do the if len 0 corner case
    int islands = 0;
    if(grid.size() == 0 || grid[0].size() == 0)
        return islands;
    if(grid.size() == 1 && grid[0].size() == 1){
        if(grid[0][0] == '1')
            islands++;
        return islands;
    }
    int m = grid.size(), n = grid[0].size();
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            islands += dfs(grid, i, j, m, n);
        }
    }
    return islands;
}
int main(int argc, char *argv[]){
    vector<vector<char>> grid;
    int m,n;
    char item;
    cin>>m>>n;
    for(int i = 0; i < m; i++){
        vector<char> row;
        for(int j = 0; j < n; j++){
            cin>>item;
            row.push_back(item);
            if(item=='1')
            cout<<item<<" ";
            else
            cout<<". ";
        }
        grid.push_back(row);
        cout<<endl;
    }
    cout<<numIslands(grid)<<endl;
    return 0;
}
