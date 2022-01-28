n = int(input())

array = []

for _ in  range(n):
    array.append(list(map(int, input().split())))

def isAll(x, y, size):
    tmp = array[x][y]
    for i in range(size):
        for j in range(size):
            if array[x+i][y+j] != tmp:
                return 2
    return tmp

first_c = 0
second_c = 0
third_c = 0

def count(x, y, size):
    global first_c
    global second_c
    global third_c

    isall = isAll(x, y, size)
    if isall == -1:
        first_c += 1
    elif isall == 0:
        second_c += 1
    elif isall == 1:
        third_c += 1
    else:
        for i in range(3):
            for j in range(3):
                count(x + i*(size//3), y + j*(size//3), size//3)

count(0, 0, n)
print(first_c)
print(second_c)
print(third_c)