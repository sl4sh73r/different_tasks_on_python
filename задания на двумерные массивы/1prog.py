n, m = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
maxi = a[0][0]
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] > maxi:
            x, y = i, j
            maxi = a[i][j]
print(x, y)
