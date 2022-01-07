n = int(input())
INF = int(1e9)

graph = []
dp = [[INF] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(3):
    dp[0][i] = graph[0][i]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][j+1], dp[i-1][j+2]) + graph[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]) + graph[i][j]
        elif j == 2:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2]) + graph[i][j]

print(min(dp[n-1]))