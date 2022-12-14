def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] =a
    else:
        parent[a] = b

n = int(input())

vertex = []
edges = []
parent = [i for i in range(n + 1)]

for _ in range(n):
    vertex.append(list(map(float, input().split())))

for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        
        x = vertex[i][0] - vertex[j][0]
        y = vertex[i][1] - vertex[j][1]
        edges.append((round((x * x + y * y) ** 0.5, 2), i + 1, j + 1))

edges.sort()

result = 0
for edge in edges:
    dist, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist

print(result)