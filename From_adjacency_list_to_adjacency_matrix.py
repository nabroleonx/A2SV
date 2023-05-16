n = int(input())

for _ in range(n):
    row = list(map(int, input().split()))
    adjacency_matrix = [0] * n
    for i in row[1:]:
        adjacency_matrix[i - 1] = 1

    print(*adjacency_matrix)
