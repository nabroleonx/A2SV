n, k = map(int, input().split())
a = list(map(int, input().split()))
 
sub_sums = [0] * (n + 1)
for i in range(1, n + 1):
    sub_sums[i] = sub_sums[i - 1] + a[i - 1]
 
max_cost = sum(a)
 
partial_sums = []
for i in range(n - 1, 0, -1):
    partial_sums.append(max_cost - sub_sums[i])
 
partial_sums.sort(reverse=True)
 
for i in range(k - 1):
    max_cost += partial_sums[i]
 
print(max_cost)
