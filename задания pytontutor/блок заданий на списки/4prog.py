a = [int(s) for s in input().split()]
for i in range(1, len(a)):
    if 0<( a[i - 1]*a[i]):
        print(a[i-1], a[i])
        break
