# Problem: https://codeforces.com/problemset/problem/977/C

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
if k == 0:
    if a[0] <= 1:
        print(-1)
    else:
        print(1)
else:
    count = 0
    target = a[k-1]
    for i in range(n):
        if a[i] > target:
            break
        count += 1
    if count == k:
        print(target)
    else:
        print(-1)
