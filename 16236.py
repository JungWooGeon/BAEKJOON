from collections import deque

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

x, y = 0, 0
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            x = i
            y = j
            array[i][j] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y):
    global size

    q = deque()
    q.append([x, y, 0])

    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    results = []

    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] or array[nx][ny] > size:
                continue
            if array[nx][ny] < size and array[nx][ny] != 0:
                results.append([nx, ny, count+1])
                continue
            
            if len(results) != 0:
                continue

            visited[nx][ny] = True
            q.append([nx, ny, count+1])

    if len(results) == 0:
        return -1, -1, 0
    else:
        results.sort(key=lambda x: (x[2], x[0], x[1]))
        return results[0][0], results[0][1], results[0][2]

size, need = 2, 2
result = 0
while True:
    x, y, count = bfs(x, y)
    if x == -1 and y == -1:
        break
    else:
        array[x][y] = 0
        result += count
        need -= 1
        if need == 0:
            size += 1
            need = size

print(result)