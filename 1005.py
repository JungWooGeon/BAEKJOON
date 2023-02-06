from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    # 초기 queue 셋팅
    q = deque()
    for i in range(1, n + 1):
        # 건물 짓는 시간이 0초일 경우
        if time[i] == 0:
            for g in graph[i]:
                indegree[g] -= 1

                if indegree[g] == 0:
                    q.append((g, 0))

        # 건물 짓는 시간이 0초가 아니면서 차수가 0일 경우
        elif indegree[i] == 0:
            q.append((i, 0))

    while q:
        x, count = q.popleft()

        if x == w:
            print(count + time[x])
            break

        time[x] -= 1

        # 건물 짓기를 완료하였을 경우
        if time[x] <= 0:
            for g in graph[x]:
                indegree[g] -= 1

                if indegree[g] == 0 and time[x] == 0:
                    q.append((g, count + 1))
                elif indegree[g] == 0 and time[x] == -1:
                    # 건물 짓는 시간이 처음부터 0초일 경우
                    q.appendleft((g, count))
        
        else:
            q.append((x, count + 1))