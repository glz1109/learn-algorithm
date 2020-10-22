from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # while n:
        #     if n & 1:
        #         res = res + 1
        #     n = n >> 1
        # return res

        res = 0
        while n:
            res = res + 1
            n = n & (n - 1)
        return res

    # 递推, x & (x - 1) 去掉了x最低位的1, x & (x - 1)再加上 1 就是 x 内 1 的个数
    # x & (x - 1) 一定比 x 小, 在循环中已经推导出来由结果
    def countBits(self, num: int) -> List[int]:
        count = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            count[i] = count[i & (i - 1)] + 1
        return count

if __name__ == "__main__":
    sol = Solution()
    # print(sol.hammingWeight(127))

    # print(sol.hammingWeight(65535))

    # print(sol.hammingWeight(9999))
    
    print(sol.countBits(15))

