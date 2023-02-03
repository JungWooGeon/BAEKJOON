import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, previous):
    visited[x] = True
    previous.append(x)

    if visited[graph[x]]:
        if graph[x] in previous:
            return len(previous) - previous.index(graph[x])
        else:
            return 0
    else:
        return dfs(graph[x], previous)

t = int(input())

results = []
for _ in range(t):
    n = int(input())

    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            count += dfs(i, [])
    
    results.append(n - count)

for result in results:
    print(result)