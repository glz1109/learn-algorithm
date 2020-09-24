# 有效括号, 栈的应用
'''
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''

def isValid(s: str) -> bool:
        stack = []
        for c in s:
            # print(c)
            if c == '('  or c == '[' or c == '{':
                stack.append(c)
                # print(stack)                
            elif stack == []:
                return False
            else:
                cs = stack.pop()
                # print('stack is not none', c, cs)
                if c==')' and cs != '(':
                    return False
                if c==']' and cs != '[':
                    return False
                if c=='}' and cs != '{':
                    return False
        # print(stack)
        return not stack

# 利用栈来处理, 左括号一直入栈，碰到右括号, 弹出栈顶扩展, 如果是匹配的左括号, 继续操作
# 如果括号全部匹配, 栈最后为空; 不完全匹配, 栈不为空
def isValid_1(s: str) -> bool:
    stack = []
    paren_map = {')': '(', ']': '[', '}': '{'} # 括号映射， 右括号在前
    for c in s:
        if c not in paren_map:  # c不在map的key中, 证明是左括号, 直接入栈
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():  # 右括号, 如果栈为空，则字符串为无效括号; 
                                                        # 如果栈顶不是匹配的左括号, 也为无效括号
            return False
    return not stack    # 栈为空，所有括号匹配, 返回True; 否则返回False

if __name__ == '__main__':
    # s = '(){'
    # print(isValid(s))

    # s = '((()))'
    # print(isValid(s))

    # str = '((([{}])))'
    # print(isValid(str))

    # s = '(])'
    # print(isValid(s))

    s = '(){'
    print(isValid_1(s))

    s = '((()))'
    print(isValid_1(s))

    str = '((([{}])))'
    print(isValid_1(str))

    s = '(])'
    print(isValid_1(s))
