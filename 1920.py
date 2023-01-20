import sys

sys.setrecursionlimit(10 ** 6)

def binary_search(x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if x < a[mid]:
        return binary_search(x, start, mid - 1)
    elif x > a[mid]:
        return binary_search(x, mid + 1, end)
    else:
        return a[mid]

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in range(m):
    print(0 if binary_search(b[i], 0, n - 1) == -1 else 1)
    