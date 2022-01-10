from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs_result = []
bfs_result = []

def dfs(x, visited):
    visited[x] = True
    dfs_result.append(x)

    for g in graph[x]:
        if visited[g]:
            continue
        dfs(g, visited)

def bfs(x, visited):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        if visited[x]:
            continue
        visited[x] = True
        bfs_result.append(x)

        for g in graph[x]:
            if visited[g]:
                continue
            q.append(g)
        
visited = [False] * (n+1)
dfs(v, visited)
visited = [False] * (n+1)
bfs(v, visited)

for i in range(len(dfs_result)):
    if i == len(dfs_result) - 1:
        print(dfs_result[i])
    else:
        print(dfs_result[i], end=" ")

for i in range(len(bfs_result)):
    if i == len(bfs_result) - 1:
        print(bfs_result[i])
    else:
        print(bfs_result[i], end=" ")