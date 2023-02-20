class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, i = 0, 0
        for j in range(len(nums)):
            k -= nums[j] == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
            res = j - i + 1
        return res