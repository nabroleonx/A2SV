class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: 
            return sum(nums) 
        
        rob_last, prev = 0, 0 
        for num in nums[1:]:
            rob_last, prev = max(num + prev, rob_last), rob_last 
        
        nums[-1] = 0
        rob_first, prev = 0, 0 
        for num in nums: 
            rob_first, prev = max(num + prev, rob_first), rob_first 
        
        return max(rob_last, rob_first)