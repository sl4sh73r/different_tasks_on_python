a = [int(i) for i in input().split()]
for i in range(len(a)):
    s = a.count(a[i])
    if s == 1:
        print(a[i])
