n, m = map(int, input().split())
degrees = [0] * (n + 1)
for i in range(m):
    i, j = map(int, input().split())
    degrees[i] += 1
    degrees[j] += 1
degrees.sort()
if degrees[-1] == degrees[1]:
    print("YES")
else:
    print("NO")
