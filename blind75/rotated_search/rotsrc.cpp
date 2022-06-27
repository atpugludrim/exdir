#include<iostream>
#include<vector>
using namespace std;
int bsearch(vector<int> &arr, const int &key, const int &low, const int &high){
    if(low >= high)
        return -1;
    if(arr[low] == key)
        return low;
    else if(arr[high] == key)
        return high;
    int mid = (low + high) / 2;
    if(mid == low || mid == high){
        return -1;
    }
    else if(arr[mid] < key){
        return bsearch(arr,key,mid+1,high);
    }
    else
        return bsearch(arr,key,low,mid-1);
}
int find_switch(vector<int> &arr, const int &low, const int &high, const int &n){
    if(low>=high)
        return -1;
    else if(low>(n-1))
        return -1;
    else if(high < 0)
        return -1;
    int mid = (low + high) / 2;
    if(arr[mid]>arr[mid+1])
        return mid;
    else if(mid == low || mid == high)
        return -1;
    else if(arr[low] < arr[mid])
        return find_switch(arr, mid, high, n);
    else
        return find_switch(arr, low, mid, n);
}
int search(vector<int>& nums, int target){
    int n = nums.size();
    int switch_ind = find_switch(nums,0,n-1,n);
    int idx = -1;
    if(switch_ind == -1){
        idx = bsearch(nums, target, 0, n-1);
    }
    else{
        idx = bsearch(nums, target, 0, switch_ind);
        if(idx == -1){
            idx = bsearch(nums, target, switch_ind+1, n-1);
        }
    }
    return idx;
}
