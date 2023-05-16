n = int(input())

for i in range(n):
    row = list(map(int, input().split()))

    adj = []
    for j in range(n):
        if row[j] == 1:
            adj.append(j + 1)

    print(len(adj), *adj)
