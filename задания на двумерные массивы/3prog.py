n, m = input().split()

for i in range(int(n)):
    str = ''
    for j in range(int(m)):
        str = str + ('.' if (j % 2 != 0 if i % 2 != 0 else j % 2 == 0  ) else '*') + ' '
    print(str.strip())
