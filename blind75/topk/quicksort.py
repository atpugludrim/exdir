import numpy as np
import sys
from time import perf_counter
np.random.seed(int(sys.argv[1]))
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, low, high):
    pivot_loc = np.random.randint(low,high+1)
    swap(arr, pivot_loc, high)
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] > pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1


def topkusingpartition(arr,low,high,k):
    if low < high:
        p = partition(arr, low, high)
        # import pdb;pdb.set_trace()
        if p < k:
            topkusingpartition(arr,p+1,high,k)
        elif p > k:
            topkusingpartition(arr,low,p-1,k)


minval = 1
maxval = 10000
arrlen = 400
k = 20
arr = np.random.randint(minval,maxval,(arrlen,))
print(arr)
# quicksort(arr,0,len(arr)-1)
t_start = perf_counter()
topkusingpartition(arr,0,len(arr)-1,k)
t_end = perf_counter()
print(np.sort(arr[:k]))
print(np.sort(arr)[-k:])
print(t_end - t_start)
