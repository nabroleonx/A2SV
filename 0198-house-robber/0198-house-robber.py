class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = nums[0]
        not_rob = 0
        
        for num in nums[1:]:
            current_rob = max(num + not_rob, rob)
            not_rob = rob
            rob = current_rob
            
        return rob
