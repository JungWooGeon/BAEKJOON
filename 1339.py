n = int(input())

strings = []
array = []
d = [0] * 26

for _ in range(n):
    st = str(input())
    strings.append(st)

    for i in range(len(st)-1, -1, -1):
        d[ord(st[i])-65] = d[ord(st[i])-65] + pow(10, len(st)-i-1)


for i in range(len(d)):
    if d[i] == 0:
        continue
    array.append([d[i], chr(i+65)])

array.sort(reverse=True)

dic = dict()
value = 9
for a in array:
    dic[a[1]] = value
    value = value -1

result = 0
for string in strings:
    tmp = ""
    for s in string:
        tmp = tmp + str(dic[s])
    
    result = result + int(tmp)
    
print(result)