N = int(input())
M = int(input())
x = int(input())
y = int(input())

print(min(x, y, min(N, M)-x, max(N, M)-y))
