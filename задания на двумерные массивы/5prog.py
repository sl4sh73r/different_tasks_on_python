n = int(input())
a = [['0'] * (n - i - 1) + [1] + [2] * i for i in range(n)]
for street in a:
    print(' '.join([str(i) for i in street]))
