import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n)]

result = 0
for i in range(m):
    a, b = map(int, input().split())

    if result != 0:
        continue

    if find_parent(parent, a) == find_parent(parent, b):
        result = i + 1
    else:
        union_parent(parent, a, b)

print(result)