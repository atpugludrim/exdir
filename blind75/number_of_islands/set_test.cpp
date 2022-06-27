#include<iostream>
#include<vector>
#include<utility>
#include<set>
using namespace std;
//int numIslands(vector<vector<char>> &grid){
//    int;
//}
int main(int argc, char *argv[]){
    set<pair<int,int>> s;
    int i,j;
    while(1){
        cin>>i>>j;
        s.insert(make_pair(i,j));
        cout<<"Set contents";
        for(set<pair<int,int>>::iterator i = s.begin(); i!=s.end(); i++){
            cout<<" ("<<i->first<<", "<<i->second<<")";
        }
        cout<<endl;
    }
    return 0;
}
