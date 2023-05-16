n, m = map(int, input().split())
degrees = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1
degrees.sort()
if degrees[-1] == degrees[1]:
    print("YES")
else:
    print("NO")
