from typing import List

# 二分查找
def bsearch(arr: List[int], value: int):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        print(arr[low:high])
        mid = low + (high-low) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 二分查找 递归
def bsearch_r(arr: List[int], value: int):
    return _bsearch_recursion(arr, 0, len(arr), value)

def _bsearch_recursion(arr: List[int], low: int, high: int, value: int):
    if low > high:
        return -1

    mid = low + (high-low) // 2
    if arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return _bsearch_recursion(arr, mid+1, high, value)
    else:
        return _bsearch_recursion(arr, low, mid-1, value)

# 二分查找 找到第一个相等的元素
def bsearch_first(arr: List[int], value: int):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or arr[mid-1] != value: # mid是数组第一个元素，或者mid前一个元素不等于搜索值, 返回mid
                return mid
            else:
                high = mid - 1
    return -1

# 二分查找 找到最后一个相等的元素
def bsearch_last(arr: List[int], value: int):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            if mid == n-1 or arr[mid+1] != value: # mid是数组最后一个元素，或者mid后一个元素不等于搜索值, 返回mid
                return mid
            else:
                low = mid + 1
    return -1

# 二分查找 找到第一个大于等于给定值的元素
def bsearch_first_greater(arr: List[int], value: int):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] >= value:           
            if mid == 0 or arr[mid-1] < value: # mid是数组第一个元素，或者mid前一个元素小于搜索值, 返回mid
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
           
    return -1

# 二分查找 查找最后一个小于等于给定值的元素
def bsearch_last_smaller(arr: List[int], value: int):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] <= value:           
            if mid == n-1 or arr[mid+1] > value: # mid是数组最后一个元素，或者mid后一个元素大于搜索值, 返回mid
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
           
    return -1


if __name__ == '__main__':
    arr = [1, 3, 9, 17, 19, 24, 31, 35, 38, 46, 49, 53, 58, 61, 63, 68, 79]
    # print(bsearch(arr, 68))

    # print(bsearch_r(arr, 68))

    # arr = [1, 3, 3, 3, 9, 9, 17, 19, 24, 31, 35, 38, 46, 49, 53, 58, 61, 63, 68, 79, 79, 79]
    # print(len(arr))   
    # print(bsearch_first(arr, 3))
    # print(bsearch_first(arr, 79))

    # arr = [1, 3, 3, 3, 9, 9, 17, 19, 24, 31, 35, 38, 46, 49, 53, 58, 61, 63, 68, 79, 79, 79]
    # print(len(arr))   
    # print(bsearch_last(arr, 3))
    # print(bsearch_last(arr, 79))

    # arr = [1, 3, 6, 9, 13, 16, 20, 23, 26, 31]
    # print(len(arr))   
    # print(bsearch_first_greater(arr, 16))
    # print(bsearch_first_greater(arr, 10))
    # print(bsearch_first_greater(arr, 49))


    # arr = [1, 3, 6, 9, 9, 9, 13, 16, 16, 16, 20, 23, 26, 31]
    # print(len(arr))   
    # print(bsearch_last_smaller(arr, 16))
    # print(bsearch_last_smaller(arr, 10))
    # print(bsearch_last_smaller(arr, 49))

    arr = [1, 3, 6, 9, 9, 9, 13, 16, 16, 16, 20, 23, 26, 31]
    print(len(arr))   
    print(bsearch_first_greater(arr, 51))
