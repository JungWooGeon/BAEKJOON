n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    remove_list = []
    for i in range(len(q)):
        remove_list.append(q[i])
        result.append(q[i])
        for j in graph[q[i]]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    for r in remove_list:
        q.remove(r)

for i in range(len(result)):
    if i == len(result)-1:
        print(result[i])
    else:
        print(result[i], end=" ")