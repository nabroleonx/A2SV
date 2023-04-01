# Problem: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
res = [0] * len(nums2)
i = 0
j = 0
sum_so_far = 0
while i < len(nums1) and j < len(nums2):
    while i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
        sum_so_far += 1
        res[j] = sum_so_far
        i += 1
    res[j] = sum_so_far
    j += 1

if j < len(nums2):
    while j < len(nums2):
        res[j] = sum_so_far
        j += 1
print(*res)
