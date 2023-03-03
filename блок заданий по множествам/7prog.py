n = int(input())
sett = {str(i) for i in range(n+1)} - {'0'}
s = input()
while s[0] != 'H':
    p = input()
    if p == 'NO':
        sett = sett - {i for i in s.split()}
    else:
        sett = sett & {i for i in s.split()}
    s = input()
print(*sorted(sett))
