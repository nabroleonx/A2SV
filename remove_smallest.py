# Problem: https://codeforces.com/problemset/problem/1399/A

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    possible = True
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
