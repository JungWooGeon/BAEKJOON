import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

k, n = map(int, input().split())

lines = []
for _ in range(k):
    lines.append(int(input()))

lines.sort()

def binary_search(start, end):
    count = 0
    mid = (start + end) // 2
    for line in lines:
        if mid == 0:
            count += line
        else:
            count += line // mid
    
    # start 와 end 가 같을 경우 이분탐색은 멈춘 후 count 확인만 하고 return
    if start == end:
        return mid if count == n else 0

    x1 = 0
    if count >= n:
        # count 값이 충족되었을 경우라도 길이가 늘어날 수 있으므로 값을 뒷부분 이분탐색까지 진행한 후 비교
        x1 = mid
        x2 = binary_search(mid + 1, end)
        return max(x1, x2)
    elif count < n:
        return binary_search(start, mid)

print(binary_search(0, lines[k - 1]))
    