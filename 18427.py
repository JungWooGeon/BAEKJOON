n, m, h = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (h + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, h + 1):
        count = 0
        for block in blocks[i - 1]:
            if block == j:
                count += 1
            elif block < j:
                count += dp[i - 1][j - block]

        dp[i][j] = dp[i - 1][j] + count

print(dp[n][h] % 10007)