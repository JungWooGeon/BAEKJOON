n, m = map(int, input().split())

graph = []

for _ in range(n):
    tmp = str(input())
    g = []
    for t in tmp:
        g.append(t)
    graph.append(g)

def count_WB(x, y):
    result = []

    for i in range(n-7):
        for j in range(m-7):
            count = 0
            for a in range(8):
                for b in range(8):
                    if (i+a+j+b) % 2 == 0:
                        if x != graph[i+a][j+b]:
                            count = count + 1
                    else:
                        if x == graph[i+a][j+b]:
                            count = count + 1
            result.append(count)

    return min(result)

print(min(count_WB("W", "B"), count_WB("B", "W")))