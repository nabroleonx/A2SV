Problem: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, firstLen_max, secondLen_max = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
        for i in range(firstLen + secondLen, len(nums)):
            firstLen_max = max(firstLen_max, nums[i - secondLen] - nums[i - firstLen - secondLen])
            secondLen_max = max(secondLen_max, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, firstLen_max + nums[i] - nums[i - secondLen], secondLen_max + nums[i] - nums[i - firstLen])
        return res
            
