def fib(n):
    k = 1
    if n > 2:
        k = fib(n - 2) + fib(n - 1)
    return k
print(fib(int(input())))
