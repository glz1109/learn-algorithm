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

if __name__ == '__main__':
    sol = Solution()
    sl = sol.generateParenthesis(3)
    print(sl)
