import numpy as np


def bsearch(arr, key, *, low, high):
    if low >= high:
        return -1
    if arr[low] == key:
        return low
    elif arr[high] == key:
        return high
    mid = (low + high)//2
    if arr[mid]==key:
        return mid
    if mid == low or mid == high:
        return -1
    if arr[mid] < key:
        return bsearch(arr, key, low=mid, high=high)
    else:
        return bsearch(arr, key, low=low, high=mid)


def find_switch(arr, *, low, high):
    if low >= high:
        return -1
    if low > len(arr)-1:
        return -1
    if high < 0:
        return -1
    mid = (low + high)//2
    if arr[mid]>arr[mid+1]:
        return mid
    if mid == low or mid == high:
        return -1
    if arr[low] < arr[mid]:
        return find_switch(arr, low=mid, high=high)
    else:
        return find_switch(arr, low=low, high=mid)


def yielder(tuple_iterable):
    for k in tuple_iterable:
        yield F"({k[1]},{k[0]})"


def main():
    testcase_len = np.random.randint(6,15)
    arr = np.sort(np.random.randint(1,154,(testcase_len,))).tolist()
    print(f"{arr = }")
    key_ind = np.random.randint(-5,testcase_len)
    rotat_ind = np.random.randint(-testcase_len//5,testcase_len+testcase_len//5)
    if rotat_ind < 0 or rotat_ind > testcase_len - 1:
        rotated_arr = arr
    else:
        rotated_arr = arr[rotat_ind:]+arr[:rotat_ind]
    if key_ind < 0:
        key = np.random.randint(500,700)
    else:
        key = rotated_arr[key_ind]
    rotated_arr = [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
    testcase_len = len(rotated_arr)
    key = 13
    print(F"{rotated_arr = }\n\n{' '.join(yielder(enumerate(rotated_arr)))}\n\n{rotat_ind = }, {testcase_len = }, {testcase_len - rotat_ind - 1 = }")
    import pdb;pdb.set_trace()
    switch = find_switch(rotated_arr, low=0, high=testcase_len-1)
    print(f"{switch = }")
    if switch == -1:
        idx = bsearch(rotated_arr, key, low=0, high=testcase_len-1)
    else:
        idx = bsearch(rotated_arr, key, low=0, high=switch)
        if idx == -1:
            idx = bsearch(rotated_arr, key, low=switch+1,high=testcase_len-1)
    if idx != -1:
        print(f"{key = }, {rotated_arr[idx] = }, {idx = }")
    else:
        print(f"{key = } not found in {rotated_arr = }")

if __name__=="__main__":
    main()
