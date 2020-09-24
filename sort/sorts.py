# sorts algo

from typing import List

# 冒泡排序
def bubble_sort(arr: List[int]):
    n = len(arr)
    if n <= 1:
        return
    
    for i in range(n):
        swap_flag = False
        for j in  range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if not swap_flag:
            return
        print(i, "sotr:", arr)

# 插入排序
def insertion_sort(arr: List[int]):
    n = len(arr)
    if n<=1:
        return

    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
        
        print(i, "sotr:", arr)        

# 选择排序
def selection_sort(arr: List[int]):
    n = len(arr)
    if n <= 1:
        return
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(i, "sotr:", arr)      


if __name__ == '__main__':
    # arr = []
    # bubblesort(arr)
    # print(arr)

    # arr = [1]
    # bubble_sort(arr)
    # print(arr)

    # arr = [20, 6, 5, 2, 7, 1, -1, 14]
    # bubble_sort(arr)
    # print(arr)
    
    # arr = []
    # insertion_sort(arr)
    # print(arr)

    # arr = [1]
    # insertion_sort(arr)
    # print(arr)

    # arr = [20, 6, 5, 2, 7, 1, -1, 14]
    # insertion_sort(arr)
    # print(arr)

    # arr = []
    # insertion_sort(arr)
    # print(arr)

    # arr = [1]
    # insertion_sort(arr)
    # print(arr)

    # arr = [20, 6, 5, 2, 7, 1, -1, 14]
    arr = [3, 5, 38, 15, 36, 26, 5, 27, 2, 38, 3, 4, 19, 44, 46, 50, 48]    
    selection_sort(arr)
    print(arr)
