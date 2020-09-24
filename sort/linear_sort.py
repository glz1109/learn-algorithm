
import math
from sorts import insertion_sort
from typing import List

# 桶排序
def bucket_sort(arr: List[int]):
    n = len(arr)
    if n<= 1: return

    minval = maxval = arr[0]
    for i in range(n):
        if arr[i] < minval:
            minval = arr[i]
        elif arr[i] > maxval:
            maxval = arr[i]
    
    # 以间隔大小10来区分不同值域
    bucket_num = (maxval - minval) // 10 + 1 # 桶的数量
    bucket_arr = [ [] for _ in range(bucket_num)]

    for i in range(n):
        k = (arr[i] - minval) // 10 # 需要放入桶的序号 0 - bucket_num-1
        bucket_arr[k].append(arr[i])
        print(k, 'bucket', bucket_arr[k])

    arr.clear()
    for i in bucket_arr:
        insertion_sort(i)
        arr.extend(i)

# 计数排序
# 稳定排序 适用于非负整数
def counting_sort(arr: List[int]):
    # 遍历数组，找到最大值
    maxval = arr[0]
    for n in arr:
        if n > maxval:
            maxval = n

    # 分配最大值+1空间
    count_arr = [ 0 for _ in range(maxval+1)]

    # 遍历数组，每个元素的值在空间对应位置计数
    for n in arr:
        count_arr[n] += 1

    # 遍历空间，依次累加空间元素
    for i in range(1, maxval+1):
        count_arr[i] = count_arr[i-1] + count_arr[i]
    
    # 申请与数组大小相同临时数组，从后向前遍历数组，数组元素对应空间的值就是临时数组的插入位置
    temp_arr = [0 for i in arr]
    for i in range(len(arr)-1, -1, -1):
        temp_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1

    # 拷贝临时数组到数组，完成排序
    arr[:] = temp_arr

# 基数排序
# 数据分割成独立的位，依次对位进行排序
def radix_sort(arr: List[int]):
    radix = 10
    k = math.ceil(math.log(max(arr)+1,radix)) # 计算最长的位数
    radix_arr= [[] for _ in range(radix)]  # 数字位0-9，分配10个数位的空间
    for i in range(k):  # 对从右至左对每个数位排序
        for j in arr:
            radix_arr[j // (radix**i) % radix].append(j)
        arr.clear()       # 清空原数组
        arr[:] = [n for a in radix_arr for n in a]  # 拷贝数位空间排序元素到原数组
        for a in radix_arr:
            a.clear()
        print(arr)
        # for a in radix_arr: # 遍历数位空间数组，依次拷贝到原数组
        #     arr.extend(a)
        #     a.clear()

# 基数排序, 按字母顺序, 需要按照最长单词个数补0, 0不影响排序, ascii中0在前面
def radix_sort_str(arr: List[str]):
    radix = 27
    k = len(max(arr, key=len)) # 计算最长的位数
    radix_arr= [[] for _ in range(radix)]  # 字母a-z，分配27个数位的空间, 包含对齐补的0

    for i in range(len(arr)):
        word = arr[i]
        if len(word) < k:
            word += '0'*(k-len(word))
        arr[i] = word
    
    for i in range(-1, -k-1, -1):  # 对从右至左对每个数位排序
        for a in radix_arr:
            a.clear()

        for j in arr:
            if j[i] == '0':
                radix_arr[ord(j[i])-0x30].append(j) 
            else:
                radix_arr[ord(j[i])-0x61].append(j) 
        arr.clear()       # 清空原数组
        arr[:] = [n for a in radix_arr for n in a]  # 拷贝数位空间排序元素到原数组
        print(arr)

    for i in range(len(arr)):
        arr[i] = arr[i].replace('0','')

    
if __name__ == '__main__':
    # arr = [6, 2, 38, 15, 36, 26, 5, 27, 2, 38, 3, 12, 22, 36, 43, 17, 19, 35, 4, 19, 6, 13, 44, 61, 50, 29, 55, 49, 56, 53, -1, -4, 25, 21]
    # bucket_sort(arr)
    # print(arr)

    # arr = [6, 2, 38, 15, 36, 26, 5, 27, 2, 38, 3, 12, 22, 36, 43, 17, 19, 35, 4, 19, 6, 13, 44, 61, 50, 29, 55, 49, 56, 53, 1, 4, 25, 21]    
    # counting_sort(arr)
    # print(arr)

    # bucket_arr = [[None for _ in range(10)] for _ in range(5)]
    # print(bucket_arr)

    # arr = [7813, 99, 123, 179, 2135, 18, 1024, 7391, 65237, 15, 9, 3721]
    # radix_sort(arr)
    # print(arr)

    arr = ['hello', 'zoom', 'grape', 'world', 'bee', 'bear', 'am', 'i', 'apple', 'pear', 'able', 'banana']
    radix_sort_str(arr)
    print(arr)