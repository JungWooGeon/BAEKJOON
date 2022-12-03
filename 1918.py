# 연산자 우선순위 계산 (연산자가 아닐시 -1)
def get_op(x):
    if x == "(":
        return 0
    if x == "*" or x == "/":
        return 1
    if x == "+" or x == "-":
        return 2
    if x == ")":
        return 3
    
    return -1

cal = str(input())
stack = []

result = ""
for c in cal:
    op = get_op(c)

    # 문자열일 경우 결과에 추가
    if op == -1:
        result += c
        continue

    # 스택이 비어있을 경우 스택에 연산자 추가
    if len(stack) == 0:
        stack.append(c)
        continue

    # ")" 일 경우 "("가 나올 때 까지 스택에서 값을 빼서 출력
    if get_op(c) == 3:
        while stack:
            x = stack.pop()
            if get_op(x) == 0:
                break
            result += x
        continue

    # 연산자 우선순위 반영하여 스택에서 연산자 pop하여 반영
    if get_op(stack[-1]) > get_op(c):
        stack.append(c)
    else:
        if get_op(stack[-1]) == 0:
            stack.append(c)
        else:
            while stack:
                if get_op(stack[-1]) == 0 or get_op(stack[-1]) > op:
                    break
                result += stack.pop()
            stack.append(c)

while stack:
    result += stack.pop()
print(result)