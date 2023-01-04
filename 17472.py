import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

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

# 섬 지역 union하기 위한 dfs
def dfs_union(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if graph[nx][ny] == 0:
            continue

        if find_parent(parent, m * x + y) != find_parent(parent, m * nx + ny):
            union_parent(parent, m * x + y, m * nx + ny)
            dfs_union(nx, ny)

# 각 섬 지역을 연결할 수 있는 다리 찾기
def dfs_find(x, y, dx, dy, count):
    nx = x + dx
    ny = y + dy

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        return

    if graph[nx][ny] == 0:
        # 바다라면 계속해서 찾기
        if dx > 0:
            dx += 1
        elif dx < 0:
            dx -= 1
        elif dy > 0:
            dy += 1
        elif dy < 0:
            dy -= 1

        dfs_find(x, y, dx, dy, count + 1)
    else:
        if count <= 1:
            return

        # 같은 섬이 아니라면 경로에 추가
        a = find_parent(parent, m * x + y)
        b = find_parent(parent, m * nx + ny)
        if a != b:
            edges.append((count, a, b))

# n, m 입력
n, m = map(int, input().split())

# parent 는 2차원 graph를 1차원으로 붙여놓은 형태
parent = [i for i in range(n * m)]
graph = []
edges = []
islands = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# graph 입력
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 섬 지역 연결 (dfs로 union)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs_union(i, j)
            islands.append((i, j))

# 섬 지역을 연결할 수 있는 다리 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            for k in range(4):
                dfs_find(i, j, dx[k], dy[k], 0)

# 크루스칼
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 연결되지 않은 섬이 있을 경우 정답은 -1
p = find_parent(parent, m * islands[0][0] + islands[0][1])
for i in range(1, len(islands)):
    x, y = islands[i]

    if p != find_parent(parent, m * x + y):
        result = -1
        break

# 결과 출력
print(result)