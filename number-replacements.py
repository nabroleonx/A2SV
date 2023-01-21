# Problem: https://codeforces.com/problemset/problem/1744/A

t = int(input())
for i in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    s = list(input())
    hashMap = {}

    works = True
    for n, m in zip(a, s):
        if n not in hashMap:
            hashMap[n] = m
        else:
            if hashMap[n] == m:
                continue
            else:
                works = False
                break
    if works:
        print("YES")
    else:
        print("NO")
