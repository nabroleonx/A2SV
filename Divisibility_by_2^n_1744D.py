# Problem: https://codeforces.com/contest/1744/problem/D

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in a:
        while i % 2 == 0:
            count += 1
            i //= 2

    ca = []
    count3 = 0
    if n >= 2:
        for i in range(2, n+1, 2):
            count2 = 0
            while i % 2 == 0:
                count2 += 1
                count3 += 1
                i //= 2

            ca.append(count2)

    if count + count3 < n:
        print(-1)
        continue

    ca.sort(reverse=True)
    cc = 0
    if count >= n:
        print(0)
    else:
        for i in ca:
            count += i
            cc += 1
            if count >= n:
                print(cc)
                break
