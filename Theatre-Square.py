# Problem: https://codeforces.com/problemset/problem/1/A

n,m,a = map(int,raw_input().split())
if n%a == 0:
    k = 0
else:
    k = 1
if m%a == 0:
    p = 0
else:
    p = 1
temp1 = (n/a)+k
temp2 = (m/a)+p
print temp1*temp2
