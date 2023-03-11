import sys

input = sys.stdin.readline

# float to int type cast error 해결 : + 0.5 (85% ~ 87% 틀렸습니다)
# python 으로는 시간초과, pypy3 는 해결 가능
while True:
    n, m = map(float, input().split())
    m = int(m * 100 + 0.5)

    if n == 0 and m == 0:
        break

    # 1.00 -> 100 으로 치환하여 dp의 index로 활용
    dp = [0] * (m + 1)
    bag = []

    for _ in range(int(n + 0.5)):
        c, p = map(float, input().split())
        p = int(p * 100 + 0.5)

        bag.append((c, p))

    # bottom-up 방식으로 dp 채워가기
    for i in range(m + 1):
        for calorie, price in bag:
            # 이전 값을 확인 할 때, index 를 벗어날 경우 continue
            if i - price < 0:
                continue

            dp[i] = max(dp[i], dp[i - price] + calorie)

    print(int(dp[m] + 0.5))