string = str(input())

temp = string.split("-")
result = 0

for i in range(len(temp)):
    tmp = temp[i].split("+")
    plus = 0
    for j in range(len(tmp)):
        plus += int(tmp[j])
    result += plus if i == 0 else -plus

print(result)