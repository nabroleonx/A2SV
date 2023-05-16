from collections import defaultdict

n = int(input())
sources = set(i + 1 for i in range(n))
sinks = set(i + 1 for i in range(n))

adjacency_list = defaultdict(list)

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            adjacency_list[i + 1].append(j + 1)

for i in adjacency_list:
    sinks.discard(i)
    for j in adjacency_list[i]:
        sources.discard(j)

print(len(sources), *sources)
print(len(sinks), *sinks)
