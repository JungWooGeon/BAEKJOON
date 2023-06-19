from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    input_list = list(map(int, input().split()))
    for i in range(1, len(input_list)):
        if i < len(input_list) - 1:
            graph[input_list[i]].append(input_list[i + 1])
        if i > 1:
            indegree[input_list[i]] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

results = []
while q:
    x = q.popleft()
    results.append(x)

    for next in graph[x]:
        indegree[next] -= 1
        
        if indegree[next] == 0:
            q.append(next)

if len(results) != n:
    print(0)
else:
    for result in results:
        print(result)