class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        
        for num in nums:
            if num-1 in nums_set:
                continue
            
            subsequence = 0
            while num in nums_set:
                subsequence += 1
                num += 1
            
            res = max(res, subsequence)
        
        return res