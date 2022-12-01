from collections import deque
import sys

# 분리 집합 메소드 (find, union)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


# 데이터 입력 및 초기화 (parent는 2차원 배열(graph)을 1차원으로 붙여놓은 형태)
input = sys.stdin.readline
r, c = map(int, input().split())
parent = [i for i in range(r * c)]
q = deque()
l1_x, l1_y, l2_x, l2_y = -1, -1, -1, -1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = []
for _ in range(r):
    graph.append(list(str(input())))


# 초기 queue와 parent 설정
for i in range(r):
    for j in range(c):
        # 얼음일 경우 continue
        if graph[i][j] == 'X':
            continue
        
        # 백조 좌표 기록
        if graph[i][j] == 'L':
            if l1_x != -1:
                l2_x, l2_y = i, j
            else:
                l1_x, l1_y = i, j

        # 물 좌표 q에 저장
        q.append((i, j, 0))

        # 물끼리 연결되어 있다면 union
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            
            if graph[nx][ny] == 'X':
                continue
            if find_parent(parent, i * c + j) != find_parent(parent, nx * c + ny):
                union_parent(parent, i * c + j, nx * c + ny)

# 처음부터 연결되어 있을 경우 정답 출력 후 종료
if find_parent(parent, l1_x * c + l1_y) == find_parent(parent, l2_x * c + l2_y):
    print(0)
    exit(0)

# q : (x 좌표, y 좌표, 현재 날짜), prvious : 이전 날짜
previous = 0
while q:
    x, y, now = q.popleft()

    # 날짜가 바뀌는 경우, 백조끼리 연결되어 있는지 확인
    if previous != now:
        previous = now
        if find_parent(parent, l1_x * c + l1_y) == find_parent(parent, l2_x * c + l2_y):
            print(previous)
            break
    
    # 주변 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        
        # 얼음으로 되어 있을 경우 얼음을 깨고, q에 넣어주기
        if graph[nx][ny] == 'X':
            graph[nx][ny] = '.'
            q.append((nx, ny, now + 1))

        # 주변 탐색한 값에서 다시 한 번 주위 값이랑 비교하여 물로 연결되어 있다면 union_parent 수행
        for j in range(4):
            nx2 = nx + dx[j]
            ny2 = ny + dy[j]

            if nx2 < 0 or ny2 < 0 or nx2 >= r or ny2 >= c:
                continue
            if graph[nx2][ny2] == '.':
                union_parent(parent, nx * c + ny, nx2 * c + ny2)

# bfs 반복문 안에서 답을 찾지 못하였을 경우, 마지막에 얼음을 깨면서 만난 것이므로 정답 출력
if not q and find_parent(parent, l1_x * c + l1_y) == find_parent(parent, l2_x * c + l2_y):
    print(previous)