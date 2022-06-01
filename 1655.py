import heapq
import sys

input = sys.stdin.readline
n = int(input())

max_q = []
min_q = []

results = []
for _ in range(n):
    x = int(input())

    if len(max_q) == len(min_q):
        heapq.heappush(max_q, -x)
    else:
        heapq.heappush(min_q, x)

    if len(min_q) != 0:
        if -max_q[0] > min_q[0]:
            a = -heapq.heappop(max_q)
            b = heapq.heappop(min_q)
            heapq.heappush(max_q, -b)
            heapq.heappush(min_q, a)

    results.append(-max_q[0])

for result in results:
    print(result)