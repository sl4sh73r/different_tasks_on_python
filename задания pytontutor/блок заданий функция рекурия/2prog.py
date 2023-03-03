def p(a, n):
    if n == 0:
        return 1
    elif n > 0:
        while n != 0:
            return a * p(a, n - 1)
    elif n < 0:
        while
    n != 0:
    return (a ** -1) * p(a, n + 1)


a = float(input())

n = int(input())
print(p(a, n))
