def getZarr(string, z):
    n = len(string)
    x, y, i = 0, 0, 0

    for k in range(1, n):
        if k > y:
            x, y = k, k
            while y < n and string[y-x] == string[y]:
                y += 1
            z[k] = y - x
            y -= 1
        else:
            i = k - x
            if z[i] < y - k + 1:
                z[k] = z[i]
            else:
                x = k
                while y < n and string[y-x] == string[y]:
                    y += 1
                z[k] = y - x
                y -= 1
    return z

string = str(input())
n = len(string)
z = getZarr(string, [0]*n)

answer = ""
for i in range(n):
    if i + z[i] == n:
        isTrue = False
        for j in range(i):
            if z[j] >= z[i]:
                isTrue = True
                break
        if isTrue:
            answer = string[i:]
            break

print(-1 if answer == "" else answer)
        