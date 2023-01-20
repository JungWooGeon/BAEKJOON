import sys

input = sys.stdin.readline

n, c = map(int, input().split())

house = [int(input()) for _ in range(n)]
house.sort()
start, end = 1, house[n - 1]
result = 0

while start <= end:
    mid = (start + end) // 2
    
    x, count = 0, 1
    for i in range(1, n):
        if house[i] >= house[x] + mid:
            count += 1
            x = i

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)