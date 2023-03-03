L = [int(i) for i in input().split()]
S = set()
for i in L:
    if i in S:
        print('YES')
    else:
        print('NO')
    S.add(i)
