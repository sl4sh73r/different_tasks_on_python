s,cot=input().split(' '),0
for i in range(1,len(s)-1):
    if int(s[i])-int(s[i-1])>0 and int(s[i])-int(s[i+1])>0:
        cot+=1
print(cot)
