import numpy as np

def check_true(x):
    return x is True
def check_false(x):
    return x is False


def find_switch(arr, *, low, high, check_fn=check_true):
    if low >= high:
        return -1
    mid = (low + high)//2
    if check_fn(arr[mid]) and not check_fn(arr[mid+1]):
        return mid
    if mid == low or mid == high:
        return -1
    if check_fn(arr[mid]):
        return find_switch(arr, low=mid, high=high, check_fn=check_fn)
    else:
        return find_switch(arr, low=low, high=mid, check_fn=check_fn)


def main():
    arr_len = np.random.randint(10,12)
    true_index = np.random.randint(-arr_len//5,arr_len+arr_len//5)
    arr = [k<true_index for k in range(arr_len)]
    print(arr,'\n','\rTrue index: {} Length: {}'.format(true_index,arr_len))
    print(find_switch(arr, low=0, high=arr_len-1))
    rotat_ind = np.random.randint(0,arr_len)
    rotated_arr = arr[rotat_ind:] + arr[:rotat_ind]
    print(rotated_arr,'Rotation index: {}'.format(rotat_ind))
    print(find_switch(rotated_arr, low=0, high=arr_len-1, check_fn=check_false))


if __name__=="__main__":
    main()
