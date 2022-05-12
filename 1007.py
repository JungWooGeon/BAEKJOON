from itertools import combinations
import sys

input = sys.stdin.readline
t = int(input())

results = []
for _ in range(t):
    n = int(input())
    graph = []

    total_x = 0
    total_y = 0

    for _ in range(n):
        x, y = map(int, input().split())
        graph.append([x, y])
        total_x = total_x + x
        total_y = total_y + y

    vertex = list(combinations(graph, n//2))
    result = int(1e9)

    for ve in vertex:
        x1, y1 = 0, 0
        for v in ve:
            x1 = x1 + v[0]
            y1 = y1 + v[1]

        x2 = total_x - x1
        y2 = total_y - y1
        result = min(result, ((x1-x2)**2 + (y1-y2)**2) ** 0.5)

    results.append(result)

for r in results:
    print(r)