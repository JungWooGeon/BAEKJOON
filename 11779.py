import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

distance = [int(1e9)] * (n + 1)
graph = [[] for _ in range(n + 1)]
# 방문 경로 기록
historys = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 (history에 방문 경로를 기록)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, 0, [start]))

    while q:
        x, dist, history = heapq.heappop(q)

        if distance[x] < dist:
            continue

        for i in graph[x]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                historys[i[0]] = history + [i[0]]
                heapq.heappush(q, (i[0], cost, history + [i[0]]))

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])
print(len(historys[end]))
for i in range(len(historys[end])):
    if i == len(historys[end]) - 1:
        print(historys[end][i])    
    else:
        print(historys[end][i], end=" ")