# Problem: https://codeforces.com/problemset/problem/69/A

n = int(input())

a, b, c = 0, 0, 0
for i in range(n):
    x, y, z = list(map(int, input().split(" ")))
    a += x
    b += y
    c += z

if a == 0 and b == 0 and c == 0:
    print("YES")
else:
    print("NO")
