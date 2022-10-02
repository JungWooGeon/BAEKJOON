import sys
from collections import deque

t = int(input())

for _ in range(t):
    commands = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    q = deque(arr)

    isTrue = True
    reverse = 0

    if n == 0:
        q = []
    
    for command in commands:
        if command == "R":
            reverse += 1
        elif command == "D":
            if len(q) == 0:
                isTrue = False
                break

            if reverse % 2 == 0:
                q.popleft()
            else:
                q.pop()

    if isTrue:
        if reverse % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
    else:
        print("error")