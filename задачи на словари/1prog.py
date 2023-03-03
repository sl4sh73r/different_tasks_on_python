a={}
for word in input().split():
    if word in a:
        a[word] = a.get(word)+1
        print(a.get(word))
    else:
        a[word]=0
        print(a.get(word))
