my_dict = {}
n = input()
for i in range(int(n)):
    candidate , votes = input().split()
    my_dict[candidate] = my_dict.get(candidate, 0) + int(votes)

for j, k in sorted(my_dict.items()):
    print(j,k)
