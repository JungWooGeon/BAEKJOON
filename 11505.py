import sys

# 세그먼트 트리 build (1000000007 미만)
def segment_tree_build(node, start, end):
    if start == end:
        tree[node] = numbers[start - 1]
    else:
        mid = (start + end) // 2
        segment_tree_build(node * 2, start, mid)
        segment_tree_build(node * 2 + 1, mid + 1, end)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007

# 세그먼트 트리에서 구간 곱 구하기
def segment_tree_rangemul(node, start, end, left, right):
    if start > right or end < left:
        return 1
    if start >= left and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    p1 = segment_tree_rangemul(node * 2, start, mid, left, right)
    p2 = segment_tree_rangemul(node * 2 + 1, mid + 1, end, left, right)
    return p1 * p2

# 세그먼트 트리에서 업데이트하기 (1000000007 미만)
def segment_tree_update(node, start, end, idx, val):
    if start == end:
        numbers[idx - 1] = val
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx and idx <= mid:
            segment_tree_update(node * 2, start, mid, idx, val)
        else:
            segment_tree_update(node * 2 + 1, mid + 1, end, idx, val)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007

input = sys.stdin.readline
n, m, k = map(int, input().split())
numbers = []
tree = [0] * (10 * n)

for _ in range(n):
    numbers.append(int(input()))

# build
segment_tree_build(1, 1, n)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        # update
        segment_tree_update(1, 1, n, b, c)
    if a == 2:
        # range
        print(segment_tree_rangemul(1, 1, n, b, c) % 1000000007)