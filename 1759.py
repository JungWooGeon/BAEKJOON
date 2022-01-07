from itertools import combinations

l, c = map(int, input().split())
alphas = list(map(str, input().split()))
alphas.sort()

list = list(combinations(alphas, l))

for li in list:
    result = ""
    ja = 0
    mo = 0
    for l in li:
        result += l
        if l == "a" or l == "i" or l == "o" or l == "u" or l == "e":
            mo += 1
        else:
            ja += 1

    if ja >= 2 and mo >= 1:
        print(result)