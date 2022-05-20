from collections import deque

t = int(input())

dx = [-2, -1, 2, 1, -2, -1, 2, 1]
dy = [-1, -2, -1, -2, 1, 2, 1, 2]

results = []
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    board = [[0] * n for _ in range(n)]

    board[start_x][start_y] = 1

    q = deque()
    q.append([start_x, start_y])

    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            results.append(board[x][y]-1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])

for result in results:
    print(result)