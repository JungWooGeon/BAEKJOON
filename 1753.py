import heapq

v, e = map(int, input().split())
k = int(input())
INF = int(1e9)

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

q = []
heapq.heappush(q, [0, k])
distance[k] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, [cost, i[0]])

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])