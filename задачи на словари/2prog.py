n = int(input())
data = dict(input().split() for i in range(n))
word = input()
if word in data.keys():
    print(data[word])
else:
    for k, v in data.items():
        if v == word:
            print(k)
            break
