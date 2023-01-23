import heapq, sys

input = sys.stdin.readline
n = int(input())

gas_station = [list(map(int, input().split())) for _ in range(n)]
gas_station.sort()

l, p = map(int, input().split())

q = [-p]
gas_station_index = 0
current = 0
result = -1
isTrue = False

while q:
    fuel = -heapq.heappop(q)

    current += fuel
    result += 1

    if current >= l:
        isTrue = True
        break

    while gas_station_index < n and gas_station[gas_station_index][0] <= current:
        heapq.heappush(q, -gas_station[gas_station_index][1])
        gas_station_index += 1

if isTrue:
    print(result)
else:
    print(-1)