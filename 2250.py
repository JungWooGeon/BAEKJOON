n = int(input())

# col, level, index
col_level = [[0, 0, i] for i in range(n+1)]

child = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    if b != -1:
        parent[b].append(a)
    if c != -1:
        parent[c].append(a)
    child[a].append(b)
    child[a].append(c)

# root node index
p_index = -1
for i in range(1, len(parent)):
    if parent[i] == []:
        p_index = i
        break

# current는 현재 column
current = 1
# i는 현재 index, l은 현재 level
def dfs(i, l):
    global current
    left, right = child[i]
    col_level[i][1] = l

    if left != -1:
        dfs(left, l+1)
    col_level[i][0] = current
    current = current + 1
    if right != -1:
        dfs(right, l+1)

dfs(p_index, 1)
col_level.sort(key=lambda x: (x[1], x[0]))


# search max value
first = 0
lev = 0
max_result = 0
result_level = 0

for i in range(1, len(col_level)):
    if lev != col_level[i][1]:
        lev = col_level[i][1]
        first = col_level[i][0]

    if i+1 >= len(col_level) or (i+1 < len(col_level) and col_level[i+1][1] != lev):
        x = col_level[i][0] - first + 1
        if max_result < x:
            max_result = x
            result_level = lev

print(result_level, max_result)