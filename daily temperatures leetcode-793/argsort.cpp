#include<iostream>
#include<vector>
#include<map>
#include<iomanip>
#include<algorithm>
#include<numeric>
#include<utility>
using namespace std;
vector<int> sort_index(const vector<int> &vec){
    vector<int> ind(vec.size());
    iota(ind.begin(), ind.end(), 0);
    sort(ind.begin(), ind.end(),
            [&vec](int i, int j) -> bool{
                return vec[i] < vec[j];
            });
    return ind;
}
int main(int argc, char *argv[]){
    int n, elem;
    vector<int> vec, idx;
    cin >> n;
    for(int i=0; i < n; i++){
        cin >> elem;
        cout << elem << " ";
        vec.push_back(elem);
    }
    cout<<"\n";
    idx = sort_index(vec);
    for(vector<int>::iterator it=idx.begin(); it!=idx.end(); it++){
        cout<<setw(2)<<*it<<" ";
    }
    cout<<"\n";
    return 0;
}
