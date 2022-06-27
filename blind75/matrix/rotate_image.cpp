#include<iostream>
#include<vector>
using namespace std;
void rotate(vector<vector<int>>&);
int main(int argc, char *argv[]){
    int n, item;
    cin >> n;
    vector<vector<int>> matrix;
    for(int i = 0; i < n; i++){
        vector<int> row;
        for(int j = 0; j < n; j++){
            cin>>item;
            row.push_back(item);
        }
        matrix.push_back(row);
    }
    rotate(matrix);
    for(vector<vector<int>>::iterator it=matrix.begin(); it!=matrix.end(); it++){
        for(vector<int>::iterator it2=it->begin(); it2!=it->end(); it2++){
            cout<<*it2<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
void rotate(vector<vector<int>> &matrix){
    // Matrix is nxn
    // Has to be inplace
    // 1. Transpose
    // 2. Reverse the column order
    // or
    // Do both in one go.
    int n = matrix.size();
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            // xor swap
            matrix[i][j] = matrix[i][j] ^ matrix[j][i];
            matrix[j][i] = matrix[i][j] ^ matrix[j][i]; // locality of reference violated
            matrix[i][j] = matrix[i][j] ^ matrix[j][i];
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n/2; j++){
            int k = n - 1 - j;
            // xor swap
            matrix[i][j] = matrix[i][j] ^ matrix[i][k];
            matrix[i][k] = matrix[i][j] ^ matrix[i][k];
            matrix[i][j] = matrix[i][j] ^ matrix[i][k];
        }
    }
}
