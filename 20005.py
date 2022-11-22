import sys
from collections import deque

input = sys.stdin.readline

m, n, p = map(int, input().split())
array = []
players = []
attack = []
distance = []
results = [False] * p
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(m):
    array.append(list(str(input())))

for i in range(m):
    for j in range(n):
        if array[i][j] != '.' and array[i][j] != 'X' and array[i][j] != 'B':
            players.append([i, j, array[i][j]])

for _ in range(p):
    tmp = list(map(str, input().split()))
    attack.append([tmp[0], int(tmp[1])])

players.sort(key=lambda x: x[2])
attack.sort()

hp = int(input())

def bfs(x, y):
    visited = [[False] * n for _ in range(m)]
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = True

    results = []

    while q:
        x, y, c = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny] or array[nx][ny] == 'X':
                continue
            
            if array[nx][ny] == 'B':
                results.append(c+1)
            if len(results) != 0:
                continue

            visited[nx][ny] = True
            q.append([nx, ny, c+1])

    return min(results)

for player in players:
    distance.append(bfs(player[0], player[1]))

all_attack = 0
while hp > 0:
    for i in range(p):
        if distance[i] == 0:
            if results[i]:
                continue
            results[i] = True
            all_attack += attack[i][1]
        else:
            distance[i] -= 1
    
    hp -= all_attack

count = 0
for r in results:
    if r:
        count += 1

print(count)