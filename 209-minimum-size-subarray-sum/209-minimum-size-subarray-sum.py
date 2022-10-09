class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)+1
        left_ptr = 0
        prefix_sum = 0
        
        if target in nums:
            return 1
        
        for i,val in enumerate(nums):
            prefix_sum += val
            while prefix_sum >= target:
                length = min(length, i-left_ptr+1)
                prefix_sum -= nums[left_ptr]
                left_ptr += 1
            
        return length if length != len(nums)+1 else 0
                