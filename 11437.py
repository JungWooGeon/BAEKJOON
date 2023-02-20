import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

# parent 와 depth 기록
def dfs(x, dep):
    # depth 기록
    depth[x] = dep
    visited[x] = True

    for g in graph[x]:
        if not visited[g]:
            # parent 기록 후 재귀적 탐색
            parent[g] = x
            dfs(g, dep + 1)

n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
depth = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    # depth 먼저 맞춰주기
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 부모로 올라가면서 LCA 탐색
    while a != b:
        a = parent[a]
        b = parent[b]

    print(a)