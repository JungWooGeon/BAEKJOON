import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

n, m, k = map(int, input().split())
psychologist = list(map(int, input().split()))
magician = list(map(int, input().split()))

psychologist.sort()

parent = [i for i in range(psychologist[-1] + 1)]

for card in magician:
    start = 0
    end = m - 1

    result = 0
    while start <= end:
        mid = (start + end) // 2
        
        if find_parent(parent, psychologist[mid]) > card:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(psychologist[result])
    union_parent(parent, 0 if result == 0 else psychologist[result - 1], psychologist[result])