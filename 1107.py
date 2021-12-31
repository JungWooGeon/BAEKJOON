from itertools import product

n = str(input())
m = int(input())

errors = []
if m != 0:
    errors = list(map(str, input().split()))

isTrue = True
for i in range(len(n)):
    if n[i] in errors:
        isTrue = False
        break

if isTrue:
    result = 100 - int(n) if 100 > int(n) else int(n) - 100
    print(min(len(n), result))
else:
    buttons = []
    for i in range(10):
        if not str(i) in errors:
            buttons.append(str(i))

    result = 100 - int(n) if 100 > int(n) else int(n) - 100

    for i in range(-1, 2):
        if len(n) - i == 0:
            continue
        word_list = list(product(buttons, repeat = len(n)-i))
        for word in word_list:
            x = ""
            for w in word:
                x += w
            count = int(n) - int(x) if int(n) > int(x) else int(x) - int(n)
            count += len(n) - i
            result = min(result, count)

    print(result)