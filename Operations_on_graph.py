from collections import defaultdict


def AddEdge(u, v):
    adj[u].append(v)
    adj[v].append(u)


def Vertex(u):
    print(*adj[u])


n = int(input())
k = int(input())

adj = defaultdict(list)

for _ in range(k):
    ops = list(map(int, input().split()))

    if ops[0] == 1:
        AddEdge(ops[1], ops[2])
    else:
        Vertex(ops[1])
