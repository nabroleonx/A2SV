class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        right = 0
        res = []
        while right < len(nums):
            left = nums[right]
            
            while right+1 < len(nums) and nums[right] + 1 == nums[right+1]:
                right += 1
            
            if left == nums[right]:
                res.append(str(nums[right]))
            else:
                res.append(str(left)+"->"+str(nums[right]))
            
            right += 1
        
        return res
            
            