n = int(input())
parent_array = list(map(int, input().split()))
delete_node = int(input())

child_array = [[] for _ in range(n)]

root = 0
for i in range(n):
    if parent_array[i] == -1:
        root = i
        continue
    child_array[parent_array[i]].append(i)

count = 0
def dfs(root):
    global count
    if child_array[root] == [] or child_array[root] == [delete_node]:
        count += 1
    for child in child_array[root]:
        if child == delete_node:
            continue
        dfs(child)
if parent_array[delete_node] == -1:
    print(0)
else:
    dfs(root)
    print(count)