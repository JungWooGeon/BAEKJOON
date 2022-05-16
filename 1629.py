a, b, c = map(int, input().split())

def modulo(a, b, c):
    if b == 1:
        return a % c 

    mid = modulo(a, b // 2, c)
    if b % 2 == 0:
        return mid * mid % c
    else:
        return mid * mid * a % c

print(modulo(a, b, c))