def p(a, n):
    if n == 0:
        return 1
    else:
        return a * p(a, n - 1)


print(p(float(input()), int(input())))
