string = str(input())
n = int(input())
cursor = len(string)

for _ in range(n):
    ins = list(map(str, input().split()))

    if len(ins) == 2:
        if cursor == 0:
            string = ins[1] + string
        elif cursor == len(string):
            string += ins[1]
        else:
            string = string[:cursor] + ins[1] + string[cursor:]
        cursor += 1
    elif ins[0] == "L":
        cursor -= 1 if cursor > 0 else cursor
    elif ins[0] == "D":
        cursor += 1 if cursor < len(string) else cursor
    elif ins[0] == "B":
        if cursor == 0:
            continue
        elif cursor == len(string):
            string = string[:cursor-1]
        else:
            string = string[:cursor-1] + string[cursor:]
        cursor -= 1

print(string)