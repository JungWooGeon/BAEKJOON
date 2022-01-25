from collections import deque
from re import L
import sys

input = sys.stdin.readline
string = str(input())
n = int(input())

left = list(string)[:-1]
right = deque()

for _ in range(n):
    ins = list(map(str, input().split()))

    if len(ins) == 2:
        left.append(ins[1])
    else:
        if ins[0] == "L":
            if len(left) > 0:
                right.insert(0, left.pop())
        elif ins[0] == "D":
            if len(right) > 0:
                left.append(right.popleft())
        elif ins[0] == "B":
            if len(left) > 0:
                left.pop()

result = ""
for l in left:
    result += l
for r in right:
    result += r
print(result)