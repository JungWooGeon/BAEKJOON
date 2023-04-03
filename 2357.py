import sys

input = sys.stdin.readline

def segment_tree_build(node, start, end):
    if start == end:
        min_tree[node] = numbers[start - 1]
        max_tree[node] = numbers[start - 1]
    else:
        mid = (start + end) // 2
        segment_tree_build(2 * node, start, mid)
        segment_tree_build(2 * node + 1, mid + 1, end)
        min_tree[node] = min(min_tree[2 * node], min_tree[2 * node + 1])
        max_tree[node] = max(max_tree[2 * node], max_tree[2 * node + 1])

def segement_tree_min_max(node, start, end, left, right):
    if start > right or end < left:
        return int(1e9), 0
    if start >= left and end <= right:
        return min_tree[node], max_tree[node]
    mid = (start + end) // 2
    min_p1, max_p1 = segement_tree_min_max(2 * node, start, mid, left, right)
    min_p2, max_p2 = segement_tree_min_max(2 * node + 1, mid + 1, end, left, right)

    return min(min_p1, min_p2), max(max_p1, max_p2)

n, m = map(int, input().split())
min_tree = [int(1e9)] * (n * 10)
max_tree = [int(1e9)] * (n * 10)
numbers = [int(input()) for _ in range(n)]
inputs = [list(map(int, input().split())) for _ in range(m)]

segment_tree_build(1, 1, n)

for a, b in inputs:
    print(" ".join(map(str, segement_tree_min_max(1, 1, n, a, b))))