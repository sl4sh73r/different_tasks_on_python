spis = input().split()
k = 0
for i in range(len(spis)):
    k += spis[i + 1:].count(spis[i])
print(k)
