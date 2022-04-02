def fib(n):
    if n < 1:
        return 0
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def fibonacci(num):
    res = []
    for n in range(1, num+1):
        res += [fib(n)]
    return res
