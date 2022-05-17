n, k = map(int, input().split())

coins = []
dp = [0] * 10001

for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    coins.append(coin)

for coin in coins:
    dp[coin] = dp[coin] + 1
    for i in range(coin+1, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])