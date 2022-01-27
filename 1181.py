n = int(input())
array = []

for _ in range(n):
    array.append(str(input()))

array = list(set(array))
array = sorted(array, key=lambda x : (len(x), x))

for arr in array:
    print(arr)