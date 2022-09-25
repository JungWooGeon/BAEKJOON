from collections import deque
import sys

input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
array = []

for _ in  range(h):
    array.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
steps = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

q = deque()
q.append((0, 0, 0, k))
visited = [[[False] * w for _ in range(h)] for _ in range(k+1)]
visited[k-1][0][0] = True
result = -1

while q:
    x, y, count, s_count = q.popleft()

    if x == h-1 and y == w-1:
        result = count
        break

    if s_count > 0:
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if visited[s_count-1][nx][ny] or array[nx][ny] == 1:
                continue
            visited[s_count-1][nx][ny] = True
            q.append((nx, ny, count+1, s_count-1))
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if visited[s_count][nx][ny] or array[nx][ny] == 1:
            continue
        visited[s_count][nx][ny] = True
        q.append((nx, ny, count+1, s_count))

print(result if result != -1 else -1)