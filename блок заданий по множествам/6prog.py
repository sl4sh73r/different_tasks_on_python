tekst = int(input())
slova = set()
for i in range(tekst):
    S = input().split()
    for elem in S:
        slova.add(elem)
print(len(slova))
