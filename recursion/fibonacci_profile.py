import cProfile

# 利用cProfile分析性能

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res

def fib_dp(n):
    res = []
    prepre = 0
    pre = 1

    for i in range(n+1):
        if i <= 1:
            res.append(i)
        else:
            cur = pre + prepre
            prepre = pre
            pre = cur
            res.append(cur)
    return res

cProfile.run('print(fib_dp(30))')

cProfile.run('print(fib_seq(30))')
