from itertools import combinations

n, s = map(int, input().split())

table = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    tmp = list(combinations(table, i))
    for t in tmp:
        if sum(t) == s:
            count += 1

print(count)