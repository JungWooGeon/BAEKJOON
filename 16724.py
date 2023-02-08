import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

n, m = map(int, input().split())
map = [str(input()) for _ in range(n)]
parent = [i for i in range(n * m)]

for i in range(n):
    for j in range(m):
        if map[i][j] == "U":
            if find_parent(parent, (i - 1) * m + j) != find_parent(parent, i * m + j):
                union_parent(parent, (i - 1) * m + j, i * m + j)
        elif map[i][j] == "D":
            if find_parent(parent, (i + 1) * m + j) != find_parent(parent, i * m + j):
                union_parent(parent, (i + 1) * m + j, i * m + j)
        elif map[i][j] == "L":
            if find_parent(parent, i * m + j - 1) != find_parent(parent, i * m + j):
                union_parent(parent, i * m + j - 1, i * m + j)
        elif map[i][j] == "R":
            if find_parent(parent, i * m + j + 1) != find_parent(parent, i * m + j):
                union_parent(parent, i * m + j + 1, i * m + j)

parent_set = set()
for i in range(n):
    for j in range(m):
        parent_set.add(find_parent(parent, i * m + j))

print(len(parent_set))