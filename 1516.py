from doctest import BLANKLINE_MARKER


n = int(input())

graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
indegree = [0] * (n+1)
result = [0] * (n+1)

for j in range(n):
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        if tmp[i] == -1:
            break
        if i == 0:
            time[j+1] = tmp[i]
        else:
            graph[tmp[i]].append(j+1)
            indegree[j+1] += 1

count = 0
q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    count += 1
    remove = []

    for i in range(len(q)):
        time[q[i]] -= 1
        if time[q[i]] == 0:
            for j in range(len(graph[q[i]])):
                indegree[graph[q[i]][j]] -= 1
                if indegree[graph[q[i]][j]] == 0:
                    q.append(graph[q[i]][j])
            result[q[i]] = count
            remove.append(q[i])
    for r in remove:
        q.remove(r)

for i in range(1, len(result)):
    print(result[i])