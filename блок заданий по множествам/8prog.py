n = set([int(i) for i in range(1,int(input())+1)])
while True:
    Str = input()
    if Str=="HELP": break
    s = set([int(i) for i in Str.split()])
    if len(s&n)>len(n)//2:
        print("YES")
        n&=s
    else:
        print("NO")
        n-=s
print(*sorted(n))

