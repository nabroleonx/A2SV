class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        max_ = 0
        for i in range(0, len(nums), 2):
            max_ += nums[i]
        
        return max_