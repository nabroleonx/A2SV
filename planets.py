# Problem: https://codeforces.com/problemset/problem/1730/A

t = int(input())

for i in range(t):
    n, c = list(map(int, input().split()))

    a = list(map(int, input().split()))
    hashMap = {}

    cost = 0
    for i in a:
        hashMap[i] = hashMap.get(i, 0) + 1
    for i in hashMap.keys():
        if hashMap[i] < c:
            cost += hashMap[i]
        else:
            cost += c
    print(cost)
