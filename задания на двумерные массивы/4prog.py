n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for street in a:
    print(' '.join([str(i) for i in street]))
