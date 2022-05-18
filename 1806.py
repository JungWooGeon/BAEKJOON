n, s = map(int, input().split())

numbers = list(map(int, input().split()))

start = 0
end = 0

result = int(1e9)
tmp = numbers[end]
while True:
    if tmp >= s:
        result = min(result, end-start+1)
        if start == end:
            break
        tmp = tmp - numbers[start]
        start = start + 1
    else:
        end = end + 1
        if end == n:
            break
        tmp = tmp + numbers[end]
        
        
if result == int(1e9):
    print(0)
else:
    print(result)