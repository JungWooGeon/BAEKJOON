ins = list(map(int, input().split()))
n = len(ins)-1
dp = [[[400001 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
dp[-1][0][0] = 0

def move(start, end):
    if start == 0:
        if end == 0:
            return 0
        else:
            return 2

    if start == end:
        return 1
    elif abs(start - end) == 1 or abs(start - end) == 3:
        return 3
    else:
        return 4

for i in range(n):
    for current in range(5):
        for start in range(5):
            add = move(start, ins[i])
            dp[i][ins[i]][current] = min(dp[i][ins[i]][current], dp[i-1][start][current] + add)
            dp[i][current][ins[i]] = min(dp[i][current][ins[i]], dp[i-1][current][start] + add)

result = int(1e9)
for l in range(5):
    for r in range(5):
        result = min(result, dp[n-1][l][r])
print(result)