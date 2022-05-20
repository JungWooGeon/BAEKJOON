n = int(input())

count = 0
results = []
def hanoi(start, mid, end, x):
    global count
    if x == 0:
        return
    count = count + 1
    hanoi(start, end, mid, x-1)
    results.append([start, end])
    hanoi(mid, start, end, x-1)

hanoi(1, 2, 3, n)
print(count)
for result in results:
    print(result[0], result[1])