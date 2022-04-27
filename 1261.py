from collections import deque

n, m = map(int, input().split())

graph = []
dp = [[int(1e9)] * n for _ in range(m)]

for _ in range(m):
    tmp = []
    numbers = str(input())
    for number in numbers:
        tmp.append(int(number))
    graph.append(tmp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    dp[x][y] = 0

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if dp[x][y] + graph[nx][ny] < dp[nx][ny]:
                dp[nx][ny] = dp[x][y] + graph[nx][ny]
                q.append([nx, ny])
            

bfs(0, 0)
print(dp[m-1][n-1])