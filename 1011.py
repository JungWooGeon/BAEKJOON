t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    d = y - x

    n = 1
    count = 0
    while d > 0:
        for _ in range(2):
            d -= n
            count += 1
            if d <= 0:
                break
        n += 1
    print(count)