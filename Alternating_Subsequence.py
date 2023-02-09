# Problem: https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pos = -float("inf")
    neg = -float("inf")
    res = 0
    for i in range(n):
        if a[i] < 0:
            neg = max(neg, a[i])
            if pos != -float("inf"):
                res += pos
                pos = -float("inf")
        else:
            pos = max(pos, a[i])
            if neg != -float("inf"):
                res += neg
                neg = -float("inf")

    if pos != -float("inf"):
        res += pos
    if neg != -float("inf"):
        res += neg

    print(res)
