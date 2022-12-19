import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(x, depth):
    visited[x] = depth
    for i in graph[x]:
        if visited[i] == -1:
            dfs(i, depth + 1)

dfs(k, 0)

for i in range(1, len(visited)):
    print(visited[i])