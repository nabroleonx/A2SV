class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        sum_ = 0
        
        for i in range(len(nums)):
            sum_ += nums[i]
            res = max(res, math.ceil(sum_ / (i + 1)))

        return res