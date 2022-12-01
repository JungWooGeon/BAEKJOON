import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
array = []
dp = [[-1] * m for _ in range(n)]

for _ in range(n):
    array.append(list(map(int, input().split())))
    

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, visited):
    global n, m
    
    dp[x][y] = 0
    
    if x == n-1 and y == m-1:
        dp[x][y] = 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if visited[nx][ny] or array[nx][ny] >= array[x][y]:
            continue
        if dp[nx][ny] == -1:
            visited[nx][ny] = True
            dfs(nx, ny, visited)
            visited[nx][ny] = False
        dp[x][y] += dp[nx][ny]
    
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
dfs(0, 0, visited)

print(dp[0][0])