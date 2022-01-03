t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = abs((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance > (r1 + r2) ** 2:
            print(0)
        elif distance == (r1 + r2) ** 2 or distance == abs(r1 - r2) ** 2:
            print(1)
        elif distance < (r1 + r2) ** 2 and distance > abs(r1 - r2) ** 2:
            print(2)
        elif distance < (r1 + r2) ** 2 and distance < abs(r1 - r2) ** 2:
            print(0)