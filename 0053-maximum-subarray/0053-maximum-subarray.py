class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = float('-inf')
        max_so_far = 0
        
        for num in nums:
            if max_so_far > 0:
                max_so_far += num
            else:
                max_so_far = num
            
            max_ = max(max_so_far, max_)
        
        return max_