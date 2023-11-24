class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return nums[i]
        