a = [int(s) for s in input().split()]
Pet = int(input())
Petpos = 1
for i in range(len(a)):
    if Pet <= a[i]:
        Petpos += 1
print(Petpos)
