a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
k = b[0]
c = b[1]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = c
print(' '.join([str(i) for i in a]))
