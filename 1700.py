n, k = map(int, input().split())
elect = list(map(int, input().split()))

powerstrip = []
result = 0

for i in range(k):
    # 이미 연결되어 있는 경우
    if elect[i] in powerstrip:
        continue

    if len(powerstrip) < n:
        # 멀티탭에 자리가 있는 경우
        powerstrip.append(elect[i])
    else:
        # 멀티탭에 자리가 없는 경우 마지막에 있거나 안나온 부분 찾기
        visited = [False] * n
        index = -1
        for j in range(i + 1, k):
            for l in range(n):
                if not visited[l] and powerstrip[l] == elect[j]:
                    index = l
                    visited[index] = True
        
        # 안나온 부분이 있다면 뽑을 곳으로 설정
        for j in range(n):
            if not visited[j]:
                index = j
                break
            
        powerstrip[index] = elect[i]
        result += 1

print(result)