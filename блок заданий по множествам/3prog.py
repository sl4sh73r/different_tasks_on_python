A = sorted(list(set([int(s) for s in input().split()]) & set([int(s) for s in input().split()])))
for elem in A:
    print(elem, end=' ')
