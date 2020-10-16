# 斐波拉契数列
# 0 1 1 2 3 5....

# 递归 n-->0
def fib_recursion(n):
    if n == 0 or n == 1:
        return n      
    return fib_recursion(n-1) + fib_recursion(n-2)

# 带备忘录的递归fib
def fib_recursion_memo(n):
    visit = [-1 for _ in range(0, n+1)]  

    def _fib(n):
        if n == 0 or n == 1:
            visit[n] = n
            return n      
        
        if visit[n] != -1:
            return visit[n]

        res = _fib(n-1) + _fib(n-2)
        visit[n] = res

        return  res
    
    return _fib(n)


# 动态规划 - 与递归相反 0-->n
def fib_dp(n):
    result = list(range(n+1))

    for i in range(n+1):
        if i<2:
            result[i] = i
        else:
            result[i] = result[i-1] + result[i-2]
    print(result)
    return result[-1]

def fib_dp_compress_arr_1(n):
    pre = 0
    prepre = 1
    res = 0

    for i in range(n):
        res = pre + prepre
        prepre = pre
        pre = res        

    return res

def fib_dp_compress_arr_2(n):   
    fn_2 = 0
    fn_1 = 1

    for i in range(n):
        fn_2, fn_1 = fn_1, fn_2+fn_1
    return fn_2

if __name__ == '__main__':
    res = fib_recursion(10)
    print(res)

    # res = fib_recursion_memo(40)   
    # print(res)

    # res = fib_dp(30)
    # print(res)

    res = fib_dp_compress_arr_1(10)
    print(res)    

    res = fib_dp_compress_arr_2(1)
    print(res)        