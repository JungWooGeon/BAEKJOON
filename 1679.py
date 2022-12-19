from collections import deque

n = int(input())
numbers = list(map(int, input().split()))

dp = [int(1e9)] * 1001
q = deque()
k = int(input())

for number in numbers:
    q.append((number, 1))

while q:
    x, count = q.popleft()

    dp[x] = min(dp[x], count)

    if count == k:
        continue

    for number in numbers:
        if dp[x + number] > count + 1:
            q.append((x + number, count + 1))

for i in range(1, 1001):
    if dp[i] == int(1e9):
        print("jjaksoon" if i % 2 != 0 else "holsoon", end="")
        print(" win at", i)
        break