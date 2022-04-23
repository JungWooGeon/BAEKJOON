from sys import stdin
import heapq

input = stdin.readline

n, k = map(int, input().split())

jew = []
bag = []
q = []

for _ in range(n):
    jew.append(list(map(int, input().split())))

for _ in range(k):
    bag.append(int(input()))

bag.sort()
jew.sort()

result = 0
index = 0
for b in bag:
    while index < len(jew) and jew[index][0] <= b:
        heapq.heappush(q, -jew[index][1])
        index = index + 1
    if q:
        result = result + (-heapq.heappop(q))
print(result)