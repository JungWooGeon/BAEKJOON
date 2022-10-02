import sys

sys.setrecursionlimit(10**6)

n = int(input())
array = []

for _ in range(n):
    array.append(list(str(input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

def dfs1(x, y, rgb):
    visited1[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if visited1[nx][ny] or array[nx][ny] != rgb:
            continue

        dfs1(nx, ny, rgb)

def dfs2(x, y, rgb):
    visited2[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited2[nx][ny]:
            continue
        if (rgb == "R" and array[nx][ny] == "G") or (rgb == "G" and array[nx][ny] == "R") or rgb == array[nx][ny]:
            dfs2(nx, ny, rgb)

result1 = 0
result2 = 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs1(i, j, array[i][j])
            result1 += 1
        if not visited2[i][j]:
            dfs2(i, j, array[i][j])
            result2 += 1

print(result1, result2)