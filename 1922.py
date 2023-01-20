import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())

    graph[a].append((b, cost))
    graph[b].append((a, cost))

q = []
heapq.heappush(q, (0, 1))

result = 0

while q:
    cost, x = heapq.heappop(q)

    # 이미 방문한 곳이면 무시
    if visited[x]:
        continue

    visited[x] = True

    # q 에 이 정점에서 갈 수 있는 부분 모두 넣어주기
    for i in graph[x]:
        if not visited[i[0]]:
            heapq.heappush(q, (i[1], i[0]))

    result += cost

print(result)