from collections import deque

m, n = map(int, input().split())

array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            q.append([i, j, 0])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
while q:
    x, y, count = q.popleft()
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if array[nx][ny] == 1 or array[nx][ny] == -1:
            continue
        array[nx][ny] = 1
        q.append([nx, ny, count+1])

for arr in array:
    if 0 in arr:
        print(-1)
        exit(0)

print(result)