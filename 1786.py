def getZarr(string, z):
    n = len(string)
    x, y, i = 0, 0, 0
    
    for k in range(1, n):
        if k > y:
            x, y = k, k
            while y < n and string[y-x] == string[y]:
                y += 1
            z[k] = y-x
            y -= 1
        else:
            i = k - x
            if z[i] < y-k+1:
                z[k] = z[i]
            else:
                x = k
                while y < n and string[y-x] == string[y]:
                    y += 1
                z[k] = y-x
                y -= 1
    
    return z

t = str(input())
p = str(input())
z = getZarr(p+"#"+t, [0] * (len(t)+len(p)+1))

results = []
count = 0
for i in range(len(p)+1, len(p)+len(t)+1):
    if z[i] == len(p):
        count += 1
        results.append(i - len(p))

print(count)
for i in range(len(results)):
    if i == len(results)-1:
        print(results[i])
    else:
        print(results[i], end=" ")