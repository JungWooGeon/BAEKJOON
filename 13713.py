import sys

def get_z_arr(n, string, z):
    x, y, i = 0, 0, 0

    for k in range(1, n):
        if k > y:
            x, y = k, k
            while y < n and string[y - x] == string[y]:
                y += 1
            z[k] = y - x
            y -= 1
        else:
            i = k - x
            if z[i] < y - k + 1:
                z[k] = z[i]
            else:
                x = k
                while y < n and string[y - x] == string[y]:
                    y += 1
                z[k] = y - x
                y -= 1

    return z

string = str(input())
n = len(string)
m = int(sys.stdin.readline())
z = get_z_arr(n, string[::-1], [0] * n)
z[0] = n

for _ in range(m):
    print(z[n - int(input())])