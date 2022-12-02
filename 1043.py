# 분리 집합 (union, find)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

# 진실을 알고 있는 사람들은 같은 집합으로 설정
tmp = list(map(int, input().split()))
for i in range(2, len(tmp)):
    if find_parent(parent, tmp[1]) != find_parent(parent, tmp[i]):
        union_parent(parent, tmp[1], tmp[i])

# 파티 입력
parties = []
for _ in range(m):
    party = list(map(int, input().split()))

    # 파티에 같이 온 사람들은 같은 집합으로 설정
    for i in range(2, len(party)):
        if find_parent(parent, party[1]) != find_parent(parent, party[i]):
            union_parent(parent, party[1], party[i])
    parties.append(party)

# 진실을 알고 있는 사람이 없으면 정답 출력
if tmp[0] == 0:
    print(m)
    exit(0)

# 진실 집합의 부모
truth_p = find_parent(parent, tmp[1])

# 파티 탐색하며 진실 집합에 속해있지 않으면 정답으로 카운트
result = 0
for party in parties:
    if truth_p != find_parent(parent, party[1]):
        result += 1

print(result)