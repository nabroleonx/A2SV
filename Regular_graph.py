n, m = map(int, input().split())
degree = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    degree[u] += 1
    degree[v] += 1
degree.sort()
if degree[0] == degree[-1]:
    print("YES")
else:
    print("NO")
