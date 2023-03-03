N, K = [int(s) for s in input().split()]
kegli = ['I' for i in range(N)]
for i in range(K):
    l, r = [int(s) for s in input().split()]
    n = r - l
    kegli[l-1:r] = ['.' for n in range(n+1)]
print(''.join([str(i) for i in kegli]))
