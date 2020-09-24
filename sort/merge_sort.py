
from typing import List

# 归并排序, 递归方法
# 数组分成两半，分别对两个数字递归操作，进行归并，最后把排序好的子序列两两合并
# 合并过程需要申请额外的存储空间临时存放合并后的有序元素，再拷贝到原数组中
# 稳定排序
def merge_sort(arr: List[int]):
    _merge_sort(arr, 0, len(arr)-1)

def _merge_sort(arr: List[int], l: int, r: int):
    print('_merge_sort', l, r)
    if l >= r:
        return

    mid = l + ((r-l)>>1) # (r-l)>>1 r,l, 不使用(r+l)/2是防止溢出; 大数据量时, 移位效率更高
    # mid = l + (r - l) // 2
    _merge_sort(arr, l, mid)
    _merge_sort(arr, mid+1, r)
    _merge(arr, l, mid, r)

def _merge(arr: List[int], l: int, mid: int, r: int):
    print('merge', l, mid, r)
    tmp = [0 for _ in range(r-l+1)]
    n = 0

    i,j = l, mid+1
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp[n] = arr[i]
            i += 1
        else:
            tmp[n] = arr[j]
            j += 1
        n += 1

    while i <= mid:
        tmp[n] = arr[i]
        i += 1
        n += 1
    
    while j <= r:
        tmp[n] = arr[j]
        j += 1
        n += 1

    i, n = l, 0
    while i < r+1:
        arr[i] = tmp[n]
        i += 1
        n += 1

# 归并排序， 迭代方法
# sz = 1 2个一组排序
# sz = 2 4个一组排序
# sz = 3 8个一组排序
def merge_sort_iteration(arr: List[int]):
    n = len(arr)
    sz = 1
    while sz < n:
        print('sz:', sz)
        i = 0
        while i < n-1:
            print('i:', i)
            _merge(arr, i, i+sz-1, min(i+sz+sz-1,n-1))
            i += sz*2

        sz = sz * 2
        print(arr)
        print(' ')


if __name__ == '__main__':
    # arr = [6, 2, 38, 15, 36, 26, 5, 27, 2, 38, 3, 4, 19, 44, 46, 50, 48]    
    # merge_sort(arr)
    # print(arr)

    # arr = [6, 2, 38, 15, 36, 26, 5, 27, 2, 38, 3, 4, 19, 44, 61, 50, 29]    
    arr = [9, 2, 10, 5, 7, 3, 1]    
    merge_sort_iteration(arr)
    print(arr)
