#include<iostream>
#include<string>
#include<map>
#include<utility>
using namespace std;
map<pair<int, int>, int> dp_cache;
int lcs_util(string text1, string text2, const int &i, const int &j){
    map<pair<int,int>,int>::iterator it = dp_cache.find(make_pair(i, j));
    if(it != dp_cache.end())
        return it->second;
    else{
        if(i == -1 || j == -1){
            dp_cache.insert(it, make_pair(make_pair(i, j), 0));
            return 0;
        }
        else if(text1[i] == text2[j]){
            int ret = lcs_util(text1, text2, i - 1, j - 1) + 1;
            dp_cache.insert(it, make_pair(make_pair(i, j), ret));
            return ret;
        }
        else{
            int tmp1, tmp2, ret;
            tmp1 = lcs_util(text1, text2, i - 1, j);
            tmp2 = lcs_util(text1, text2, i, j - 1);
            ret = tmp1 > tmp2 ? tmp1 : tmp2;
            dp_cache.insert(it, make_pair(make_pair(i, j), ret));
            return ret;
        }
    }
}
int lcs(string text1, string text2){
    int l1 = text1.length();
    int l2 = text2.length();
    //cout<<l1<<" "<<l2<<"\n";
    return lcs_util(text1, text2, l1 - 1, l2 - 1);
}
int main(int argc, char *argv[]){
    string text1, text2;
    getline(cin, text1);
    getline(cin, text2);
    cout<<lcs(text1, text2)<<'\n';
    /*
     * for(auto i=dp_cache.begin(); i!=dp_cache.end(); i++){
     *    cout<<i->first.first<<' '<<i->first.second<<' '<<i->second<<'\n';
     *}
     */
    return 0;
}
