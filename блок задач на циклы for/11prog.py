n = int(input())
sum1 = n
sum2 = 0
for i in range(1, n):
    sum1 += i
    sum2 += int(input())
print(sum1 - sum2)
