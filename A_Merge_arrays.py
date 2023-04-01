# Problem: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
res = []
i = 0
j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        res.append(nums1[i])
        i += 1
    else:
        res.append(nums2[j])
        j += 1
if i < len(nums1):
    res += nums1[i:]
if j < len(nums2):
    res += nums2[j:]

print(*res)
