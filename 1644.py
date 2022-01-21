from collections import deque
import math

n = int(input())
array = [True for _ in range(n+1)]
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

numbers = deque()
result = 0
for i in range(2, n+1):
    if array[i]:
        numbers.append(i)

        s = sum(numbers)
        while s >= n:
            if s == n:
                result += 1
            numbers.popleft()
            s = sum(numbers)

print(result)