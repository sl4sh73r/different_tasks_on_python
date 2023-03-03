n = int(input())
mid = n // 2
a = [['.'] * n for i in range(n)]
for i in range(mid, mid + 1):
    for j in range(n):
        a[i][j] = '*'
for i in range(n):
    for j in range(mid, mid + 1):
        a[i][j] = '*'
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = '*'
for i in range(n):
    for j in range(n - i - 1, n - i):
        a[i][j] = '*'
for r in a:
    print(' '.join([str(elem) for elem in r]))
