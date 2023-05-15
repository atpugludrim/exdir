#include<iostream>
#include<map>
#include<utility>
using namespace std;
int main(int argc, char* argv[]){
    map<pair<int,int>, int> m;
    m[make_pair(4,5)]= 6;
    cout<<m[make_pair(4,5)]<<endl;
    return 0;
}
