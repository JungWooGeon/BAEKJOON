import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
q = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

results = []
while q:
    x = heapq.heappop(q)
    results.append(x)

    for g in graph[x]:
        indegree[g] -= 1
        if indegree[g] == 0:
            heapq.heappush(q, g)

print(" ".join(map(str, results)))