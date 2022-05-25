n = int(input())

array = []
dp = [0] * (n+1)

for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(n-1, -1, -1):
    if i + array[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+array[i][0]]+array[i][1])

print(dp[0])