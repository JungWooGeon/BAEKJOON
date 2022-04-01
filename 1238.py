import heapq

n, m, x = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(x):
    q = []
    distance = [INF] * (n+1)
    distance[x] = 0

    heapq.heappush(q, [0, x])

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return distance

dis_list = []
result = []
for i in range(1, n+1):
    dis_list.append(dijkstra(i))

for i in range(1, n+1):
    if i == x:
        continue
    result.append(dis_list[i-1][x] + dis_list[x-1][i])

print(max(result))