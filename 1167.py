import sys

sys.setrecursionlimit(10**6)
v = int(input())

graph = [[] for _ in range(v+1)]
result = 0

for _ in range(v):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1, 2):
        graph[tmp[0]].append((tmp[i], tmp[i+1]))

def dfs(i, dist, depth):
    global visited
    global result
    global index

    visited[i] = True
    if result < dist:
        index = i
        result = dist

    for g in graph[i]:
        if visited[g[0]]:
            continue
        dfs(g[0], dist + g[1], depth+1)

index = 1
for _ in range(2):
    visited = [False] * (v+1)
    dfs(index, 0, 0)

print(result)