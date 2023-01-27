A = ord('A')
r, c = map(int, input().split())

graph = [list(map(lambda x: ord(x) - A, input())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
def dfs(x, y, alpha, count):
    global result

    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        # 이미 나온 대문자 알파벳이라면 취소
        if ((alpha >> graph[nx][ny]) & 1) == 1:
            continue

        dfs(nx, ny, alpha | (1 << graph[nx][ny]) , count + 1)

dfs(0, 0, 1 << graph[0][0] , 1)

print(result)