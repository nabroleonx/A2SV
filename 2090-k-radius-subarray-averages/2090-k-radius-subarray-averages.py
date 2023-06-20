class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        sum_ = 0
        res = [-1] * len(nums)
        window = k * 2 + 1
        for i, val in enumerate(nums):
            sum_ += val
            if i >= k * 2:
                res[i - k] = sum_ // window
                sum_ -= nums[i - k * 2]
        return res