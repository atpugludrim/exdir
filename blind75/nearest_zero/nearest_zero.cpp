#include<iostream>
#include<utility>
#include<vector>
#include<queue>
#include<set>
using namespace std;
int bfs(vector<vector<int>> &mat, const int &x, const int &y, const int &m, const int &n){
    queue<pair<pair<int,int>,int>> q;
    set<pair<int,int>> s;
    int l = 0, curr_x, curr_y, next_x, next_y, dx[] = {1,-1,0,0}, dy[] = {0,0,1,-1};
    q.push(make_pair(make_pair(x,y),l));
    pair<pair<int,int>,int> item;
    pair<int,int> item_level2;
    while(!q.empty()){
        item = q.front();
        q.pop();
        item_level2 = item.first;
        l = item.second;
        curr_x = item_level2.first;
        curr_y = item_level2.second;
        if(mat[curr_y][curr_x] == 0)
            return l;
        s.insert(make_pair(curr_x, curr_y));
        for(int i = 0; i < 4; i++){
            next_x = curr_x + dx[i];
            next_y = curr_y + dy[i];
            if(0<=next_x && next_x<n && 0<=next_y && next_y<m && s.find(make_pair(next_x,next_y))==s.end()){
                q.push(make_pair(make_pair(next_x,next_y),l+1));
            }
        }
    }
    return -1;
}
vector<vector<int>> updateMatrix(vector<vector<int>> &mat){
    // solution do bfs from each node and return when zero is reached.
    int m = mat.size(), n = mat[0].size();
    if(m <= 1 && n <= 1)
        return mat;
    vector<vector<int>> ret;
    for(int i = 0; i < m; i++){
        vector<int> row;
        for(int j = 0; j < n; j++){
            if(mat[i][j] == 0)
                row.push_back(0);
            else
                row.push_back(bfs(mat,j,i,m,n));
        }
        ret.push_back(row);
    }
    return ret;
}
int main(int argc, char *argv[]){
    int m,n,item;
    cin>>m;
    cin>>n;
    vector<vector<int>> mat, ans;
    for(int i = 0; i < m; i++){
        vector<int> row;
        for(int j = 0; j < n; j++){
            cin>>item;
            row.push_back(item);
            if(item)
            cout<<item<<' ';
            else
            cout<<". ";
        }
        cout<<endl<<flush;
        mat.push_back(row);
    }
    cout<<endl;
    ans = updateMatrix(mat);
    for(vector<vector<int>>::iterator row=ans.begin(); row!=ans.end(); row++){
        for(vector<int>::iterator val=row->begin(); val!=row->end(); val++){
            cout<<*val<<' ';
        }
        cout<<endl;
    }
    return 0;
}
