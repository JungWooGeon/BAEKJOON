from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
t = int(input())
n = int(input()) 
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_list = []
b_list = []

for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += a[j]
        a_list.append(tmp)

for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += b[j]
        b_list.append(tmp)

a_list.sort()
b_list.sort()

result = 0
for a in a_list:
    result += bisect_right(b_list, t - a) - bisect_left(b_list, t - a)

print(result)