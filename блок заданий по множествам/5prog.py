m, n = ([int(i) for i in input().split()])
a, b=set(), set()
for i in range(m):
    a.add(int(input()))
for i in range(n):
    b.add(int(input()))
print(len(a.intersection(b)))
print(*sorted(a.intersection(b)))
print(len(a.difference(b)))
print(*sorted(a.difference(b)))
print(len(b.difference(a)))
print(*sorted(b.difference(a)))
