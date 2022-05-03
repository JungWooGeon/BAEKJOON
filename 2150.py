import sys

sys.setrecursionlimit(10**6)
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
graph_reverse = [[] for _ in range(v+1)]
visited = [False] * (v+1)
visited_reverse = [False] * (v+1)

result = []
stack = []
count = -1

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph_reverse[b].append(a)

def dfs(x):
    result[count].append(x)
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


def dfs_reverse(x):
    visited_reverse[x] = True
    for i in graph_reverse[x]:
        if not visited_reverse[i]:
            dfs_reverse(i)

    stack.append(x)

ind = v
while v > 0:
    if visited_reverse[v]:
        v = v - 1
        continue
    dfs_reverse(v)
    v = v - 1

while stack:
    k = stack.pop()
    if visited[k]:
        continue
    count = count + 1
    result.append([])
    dfs(k)

for i in range(len(result)):
    result[i].sort()
result.sort()

print(len(result))
for r in result:
    for i in range(len(r)):
        print(r[i], end=" ")
        if i == len(r) - 1:
            print(-1)