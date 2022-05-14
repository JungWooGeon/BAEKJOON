n, m, k = map(int, input().split())

tree = [0] * (10*n)
numbers = []
for _ in range(n):
    numbers.append(int(input()))

def segment_tree_build(node, start, end):
    if start == end:
        tree[node] = numbers[start-1]
    else:
        mid = (start + end) // 2
        segment_tree_build(2*node, start, mid)
        segment_tree_build(2*node+1, mid+1, end)
        tree[node] = tree[2*node] + tree[2*node+1]

def segment_tree_rangesum(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    p1 = segment_tree_rangesum(2*node, start, mid, left, right)
    p2 = segment_tree_rangesum(2*node+1, mid+1, end, left, right)
    return p1 + p2

def segment_tree_update(node, start, end, idx, val):
    if start == end:
        numbers[idx-1] = val
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx and idx <= mid:
            segment_tree_update(2*node, start, mid, idx, val)
        else:
            segment_tree_update(2*node+1, mid+1, end, idx, val)
        tree[node] = tree[2*node] + tree[2*node+1]


segment_tree_build(1, 1, n)
results = []
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_tree_update(1, 1, n, b, c)
    elif a == 2:
        results.append(segment_tree_rangesum(1, 1, n, b, c))

for result in results:
    print(result)