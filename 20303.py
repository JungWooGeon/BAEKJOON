import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = parent[b]
        candies[b] += candies[a]
        candies[a] = 0
        child_count[b] += child_count[a]
        child_count[a] = 0
    else:
        parent[b] = parent[a]
        candies[a] += candies[b]
        candies[b] = 0
        child_count[a] += child_count[b]
        child_count[b] = 0

n, m, k = map(int, input().split())
candies = list(map(int, input().split()))
parent = [i for i in range(n)]
child_count = [1] * n

for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a - 1) != find_parent(parent, b - 1):
        union_parent(parent, a - 1, b - 1)

bag = []
for i in range(n):
    if child_count[i] > 0:
        bag.append((child_count[i], candies[i]))

dp = [[0] * k for _ in range(len(bag) + 1)]

for i in range(1, len(bag) + 1):
    for j in range(k):
        if j - bag[i - 1][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - bag[i - 1][0]] + bag[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])