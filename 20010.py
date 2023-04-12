import sys

input = sys.stdin.readline

# 그래프의 끝으로 이동하여 ends 에 기록
def dfs_end(x, visited):
    isEnd = True
    for next, dist in graph[x]:
        if visited[next]:
            continue
        
        isEnd = False
        visited[next] = True
        end = dfs_end(next, visited)
        visited[next] = False
    
    if isEnd:
        ends.append(x)

# dfs 로 이동하며 cost 를 기록
def dfs_check(x, visited, cost):
    max_cost.append(cost)
    for next, dist in graph[x]:
        if visited[next]:
            continue

        visited[next] = True
        dfs_check(next, visited, cost + dist)
        visited[next] = False

# 유니온 파인드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

n, k = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = [[] for _ in range(n + 1)]
edges = []

for _ in range(k):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 크루스칼
edges = sorted(edges)

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        union_parent(parent, a, b)

# 전체 마을 연결 최소 비용 출력
print(result)

# 크루스칼로 완성한 그래프에서 끝 점들과 cost 목록을 담을 변수
ends = []
max_cost = [0] * (n + 1)

# dfs visited
visited = [False] * (n + 1)
visited[0] = True

# graph 상의 끝 점들 기록
dfs_end(0, visited)

# 끝 점들로부터 출발하여 cost 기록
visited[0] = False
for end in ends:
    dfs_check(end, visited, 0)

# 마을과 마을 사이의 가장 큰 경로의 비용 출력
print(max(max_cost))