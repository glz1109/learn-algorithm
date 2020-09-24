from typing import List

def quick_sort(arr: List[int]):
    _quick_sort(arr, 0, len(arr)-1)

# 快速排序
def _quick_sort(arr: List[int], left: int, right: int):
    # 返回条件
    if left >= right:
        return

    # 当前状态处理
    pivot = _partition(arr, left, right)
    print('left', left, 'right', right)
    print('after partition:', arr)

    # 下一级递归
    _quick_sort(arr, left, pivot-1)
    _quick_sort(arr, pivot+1, right)

    # 状态清除(如果需要)

# 分区处理
# 游标pivot初始指向right, 把数组分成两个部分, arr[left: i-1]是小于pivot的, arr[i: right]是待处理的
# 每次从arr[i: right]取出一个元素a[j], 与pivot比较, 小于pivot则加入到arr[left: i-1]区间尾部
# 最后交换a[i](第一个大于pivot的元素)和pivot, 返回新的pivot的位置
# i, j双指针
def _partition(arr: List[int], left: int, right: int):
    pivot, i = arr[right], left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i+1    
    arr[i], arr[right] = arr[right], arr[i]
    return i
    

if __name__ == '__main__':
    a1 = [6, 2, 38, 15, 36, 26, 5, 27, 2, 38, 3, 4, 19, 6, 13, 44, 61, 50, 29, -1, -4, 25, 21]    
    a2 = [9, 2, 10, 5, 7, 3, 1, 6]    
    a3 = []    
    a4 = [1]      
    a5 = [1, -1]              
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
