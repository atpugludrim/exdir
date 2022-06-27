#include<iostream>
#include<vector>
using namespace std;
vector<vector<int>> floodFill(vector<vector<int>>&, const int&, const int&, const int&, const int&, const int&);
int main(int argc, char* argv[]){
    vector<vector<int>> image, newImage;
    int sr, sc, newColor;
    int m, n, pv;
    cin >> m >> n;
    for(int i = 0; i < m; i++){
        vector<int> row;
        for(int j = 0; j < n; j++){
            cin>>pv;
            row.push_back(pv);
        }
        image.push_back(row);
    }
    cin >> sr >> sc;
    cin >> newColor;
    newImage = floodFill(image, sr, sc, newColor, m, n);
    for(vector<vector<int>>::iterator it = newImage.begin(); it != newImage.end(); it++){
        for(vector<int>::iterator rit = it->begin(); rit != it->end(); rit++){
            cout<<*rit<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
vector<vector<int>> floodFill(vector<vector<int>>& image, const int& sr, const int& sc, const int& newColor, const int& m, const int& n){
    vector<vector<int>>::size_type r,cr;
    vector<int>::size_type c,cc;
    vector<vector<int>> newImage(image);
    const int oldColor = image[sr][sc];
    const vector<int> dx = {1,-1,0,0};
    const vector<int> dy = {0,0,1,-1};
    vector<int> neighbour_row, neighbour_col;
    neighbour_row.push_back(sr);
    neighbour_col.push_back(sc);
    while(neighbour_row.size()!=0){
        r = *neighbour_row.begin();
        c = *neighbour_col.begin();
        newImage[r][c] = newColor;
        neighbour_row.erase(neighbour_row.begin());
        neighbour_col.erase(neighbour_col.begin());
        for(int dir = 0; dir < 4; dir++){
            cr = r+dy[dir];
            cc = c+dx[dir];
            if ( cr >= 0 && cc >= 0 && cr < m && cc < n ){
                if (newImage[cr][cc] == oldColor){
                    neighbour_row.push_back(cr);
                    neighbour_col.push_back(cc);
                }
            }
        }
    }
    /*
    for(int dir = 0; dir < 4; dir++){
        r = sr+dy[dir];
        c = sc+dx[dir];
        while(r < m && c < n && r >= 0 && c >= 0){
            if(newImage[r][c] == oldColor){
                newImage[r][c] = newColor;
            }
            else
                break;
            r += dy[dir];
            c += dx[dir];
        }
    }
    */
    /*
     * Only goes straight in a direction
     * Have to implement image based bfs
     */
    return newImage;
}
