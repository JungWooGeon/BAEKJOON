from collections import deque
import heapq

n, l = map(int, input().split())
a = list(map(int, input().split()))

dq = deque()
hq = []
delete_hq = []

q_len = l

results = []
for i in range(n):
    if len(dq) == q_len:
        x = dq.popleft()

        heapq.heappush(delete_hq, x)

        while len(hq) > 0 and len(delete_hq) > 0 and hq[0] >= delete_hq[0]:
            if hq[0] == delete_hq[0]:
                heapq.heappop(delete_hq)
            heapq.heappop(hq)

    dq.append(a[i])
    heapq.heappush(hq, a[i])
    results.append(hq[0])

print(" ".join(map(str, results)))