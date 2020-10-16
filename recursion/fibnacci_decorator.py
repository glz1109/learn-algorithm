import time
import functools

# 利用装饰器分析程序执行时间

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@log_execution_time
def fib_recursion(n):
    res = fib_seq(n)
    return res

def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res

@log_execution_time
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

print(fib_dp(30))

print(fib_recursion(30))

