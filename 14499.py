# 동서남북에 따라 사다리 상태 반영
def move(direction):
    tmp = []
    if direction == 1:
        tmp = [state[0], state[2], state[3], state[5], state[4], state[1]]
    elif direction == 2:
        tmp = [state[0], state[5], state[1], state[2], state[4], state[3]]
    elif direction == 4:
        tmp = [state[2], state[1], state[4], state[3], state[5], state[0]]
    elif direction == 3:
        tmp = [state[5], state[1], state[0], state[3], state[2], state[4]]

    return tmp

n, m, x, y, k = map(int, input().split())

# 지도 정보
array = [list(map(int, input().split())) for _ in range(n)]

# 주사위 좌표 이동 방향
step = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]

# 주사위 상태 정보
state = [0, 0, 0, 0, 0, 0]
# 주사위 상태 정보에서 아래와 위쪽을 가리키는 Index
bottom_idx, top_idx = 2, 5

# 명령어들을 입력받아 반복 수행
for command in list(map(int, input().split())):
    # 이동할 좌표
    nx, ny = x + step[command][0], y + step[command][1]

    # 이동할 좌표가 지도를 벗어나면 continue
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

    # 주사위 굴리기 (상태 이동, 좌표 이동)
    state = move(command)
    x, y = nx, ny

    # 주사위 값 복사 기능 수행
    if array[nx][ny] == 0:
        array[nx][ny] = state[bottom_idx]
    else:
        state[bottom_idx] = array[nx][ny]
        array[nx][ny] = 0

    # 주사위 상단에 있는 값 표시
    print(state[top_idx])

    #     2                      2
    # 4   1   3       ->     1   3   6
    #     5                      5
    #     6                      4
    

    #                            2
    #                 ->     6   4   1
    #                            5
    #                            3
    

    #                            1
    #                 ->     4   5   3
    #                            6
    #                            2
    

    #                            6
    #                 ->     4   2   3
    #                            1    
    #                            5