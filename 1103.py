from collections import deque
import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(input().rstrip()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0

def dfs(x, y, count):
    global result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]*int(graph[x][y])
        ny = y + dy[i]*int(graph[x][y])

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == "H" or count+1 <= dp[nx][ny]:
            continue

        if visited[nx][ny]:
            print(-1)
            exit()
        
        dp[nx][ny] = count + 1
        visited[nx][ny] = True
        dfs(nx, ny, count+1)
        visited[nx][ny] = False

dfs(0, 0, 0)
print(result + 1)