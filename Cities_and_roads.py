n = int(input())
count = 0
for i in range(n):
    row = list(map(int, input().split()))
    count += sum(row)
print(count // 2)
