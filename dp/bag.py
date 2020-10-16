from typing import List, overload

class Solution:
    '''
    背包问题
    对于一组不同重量、不可分割的物品，需要选择一些装入背包，
    在满足背包最大重量限制的前提下，背包中物品总重量的最大值是多少
    '''
    # weight 物品重量; overlad 最大重量
    def bag(self, weight: List[int], overload: int) -> int:
        maxw = 0
        num = len(weight)

        def addbag(n, w):     
            nonlocal maxw       
            if w == overload or n == num-1:
                if w >= maxw :
                    maxw = w
                return
        
            addbag(n+1, w)
            if w + weight[n+1] <= overload :
                addbag(n+1, w + weight[n+1])

        addbag(0, 0)

        return maxw

    def bagMemo(self, weight: List[int], overload: int) -> int:
        maxw = 0
        num = len(weight)

        tarstate = [[0 for _ in range(overload+1)] for _ in range(len(weight))]

        def addbag(n, w):     
            nonlocal maxw       
            if w == overload or n == num-1:
                if w > maxw :
                    maxw = w
                return
        
            if tarstate[n][w]:
                return
            tarstate[n][w] = True

            addbag(n+1, w)
            if w + weight[n+1] <= overload :
                addbag(n+1, w + weight[n+1])

        addbag(0, 0)

        return maxw

if __name__ == '__main__':
    sol = Solution()

    weight = [2, 2, 4, 6, 3]
    max_weight = sol.bag(weight, 9)
    print(max_weight)

    weight = [2, 2, 4, 6, 5]
    max_weight = sol.bagMemo(weight, 9)
    print(max_weight)