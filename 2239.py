def search(depth):
    # depth 가 z 의 범위를 초과하였을 경우 출력 후 종료
    if depth == len(z):
        for s in sudoku:
            print(''.join(map(str, s)))
        exit(0)
    
    x, y = z[depth]
    numbers = [False] * 10

    # 가로 세로 줄 탐색
    for i in range(9):
        numbers[sudoku[x][i]] = True
        numbers[sudoku[i][y]] = True

    # 사각형 탐색
    for i in range(3):
        for j in range(3):
            numbers[sudoku[i + 3 * (x // 3)][j + 3 * (y // 3)]] = True

    # 탐색해서 나오지 않은 숫자들을 모두 기록해보며 dfs
    for i in range(1, 10):
        if not numbers[i]:
            sudoku[x][y] = i
            search(depth + 1)
    
    # 탐색 종료 시 0으로 되돌리기
    sudoku[x][y] = 0

sudoku = [list(map(int, list(input()))) for _ in range(9)]
z = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

search(0)