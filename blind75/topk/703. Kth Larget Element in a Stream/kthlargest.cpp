#include<iostream>
#include<vector>
using namespace std;
class KthLargest{
    public:
        size_t k, maxk;
        vector<int> heap;
        KthLargest(int k, vector<int>& nums){
            this->k = 0;
            this->maxk = k;
            if(nums.size() > 0)
            build_heap(nums);
        }
        int add(int val){
            if(heap.size() < maxk){
                heap_insert(val);
            }
            else if(heap[0] < val){
                heap[0] = val;
                heapify(0);
            }
            return heap[0];
        }
        size_t parent(size_t idx){return (idx-1)/2;}
        size_t left(size_t idx){return 2*idx+1;}
        size_t right(size_t idx){return 2*idx+2;}//heap-property: heap[parent(i)] <= heap[i], forall i
        void build_heap(vector<int>& nums){
            size_t idx = 1;
            k = 1;
            heap.push_back(nums[0]);
            while(k < maxk && idx < nums.size()){
                heap_insert(nums[idx++]); // this should do k++
            }
            while(idx < nums.size()){
                if(nums[idx] > heap[0]){
                    heap[0] = nums[idx];
                    heapify(0);
                }
                idx++;
            }
        }
        void heapify(size_t idx){
            size_t l, r, largest, tmp;
            largest = idx;
            l = left(idx);
            r = right(idx);
            if(l < maxk && heap[l] < heap[idx])
                largest = l;
            if(r < maxk && heap[r] < heap[largest])
                largest = r;
            if(largest != idx){
                tmp = heap[largest];
                heap[largest] = heap[idx];
                heap[idx] = tmp;
                heapify(largest);
            }
        }
        void heap_insert(int& val){
            k++;
            int inf=10001;
            heap.push_back(inf);
            heap_decrease_key(k-1, val);
        }
        void heap_decrease_key(size_t idx, int &val){
            if(val > heap[idx])
                cout << "Error";
            heap[idx] = val;
            int tmp;
            while(idx > 0 && heap[parent(idx)] > heap[idx]){
                tmp = heap[idx];
                heap[idx] = heap[parent(idx)];
                heap[parent(idx)] = tmp;
                idx = parent(idx);
            }
        }
};
int main(int argc, char* argv[]){
    vector<int> nums;
    int n,v;
    int ret, k;
    cin >> k;
    cin >> n;
    while(n--){
        cin >> v;
        nums.push_back(v);
    }
    KthLargest kthLargest = KthLargest(k, nums);
    cin >> n;
    while(n--){
        cin >> v;
        ret = kthLargest.add(v);
        cout << ret << '\n';
    }
    return 0;
}
