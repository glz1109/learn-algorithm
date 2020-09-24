from typing import List, overload

class Solution:
    '''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    示例：
    输入：n = 3
    输出：[
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
        ]
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        sl = []
        def _generator(left: int, right: int, n: int, s: str):
            # print('-->', left, right, s)
            if left == n and right == n:
                print(s)
                return sl.append(s)
            
            if left < n:
                print('recur left->', left+1, right, s + '(')
                _generator(left+1, right, n, s + '(')

            if left > right:
                print('recur right->', left, right+1, s + ')')                
                _generator(left, right+1, n, s + ')') 

        _generator(0, 0, n, '')

        return sl

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
    # sl = sol.generateParenthesis(3)
    # print(sl)

    weight = [2, 2, 4, 6, 3]
    max_weight = sol.bag(weight, 9)
    print(max_weight)

    weight = [2, 2, 4, 6, 5]
    max_weight = sol.bagMemo(weight, 9)
    print(max_weight)