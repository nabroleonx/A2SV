class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 1
        for l in range(len(nums)-1):
            if nums[l] != nums[l+1]:
                nums[r] = nums[l+1]
                r += 1 
        return r
        