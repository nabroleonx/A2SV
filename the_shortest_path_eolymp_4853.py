from collections import defaultdict, deque

n, m = map(int, input().split())
a, b = map(int, input().split())

adj = defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

queue = deque([a])
prev_dict = {a: None}
path = []

while queue:
    node = queue.popleft()

    if node == b:
        break

    for neighbor in adj[node]:
        if neighbor not in prev_dict:
            prev_dict[neighbor] = node
            queue.append(neighbor)

if b not in prev_dict:
    print(-1)
    exit()

while b:
    path.append(b)
    b = prev_dict[b]


print(len(path) - 1)
print(*reversed(path))
