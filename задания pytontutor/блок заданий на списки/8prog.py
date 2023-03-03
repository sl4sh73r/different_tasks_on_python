a=input().split()
b=1
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        b+=1
print(b)
