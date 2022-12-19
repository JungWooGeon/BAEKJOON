import copy

n = int(input())
k = int(input())

sing = [set() for _ in range(n + 1)]
sing_number = 0

for _ in range(k):
    tmp = list(map(int, input().split()))

    if 1 in tmp:
        for i in range(1, tmp[0] + 1):
            sing[tmp[i]].add(sing_number)
        sing_number += 1
    else:
        temp_sings = set()
        for i in range(1, tmp[0] + 1):
            temp_sings.update(sing[tmp[i]])

        for i in range(1, tmp[0] + 1):
            sing[tmp[i]] = copy.deepcopy(temp_sings)

for i in range(1, n + 1):
    if len(sing[i]) == sing_number:
        print(i)
        