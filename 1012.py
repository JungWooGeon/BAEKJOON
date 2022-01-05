t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                count += 1
                q = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    visited[x][y] = True

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if visited[nx][ny] or graph[nx][ny] == 0:
                            continue
                        q.append((nx, ny))
    print(count)