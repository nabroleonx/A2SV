# Problem: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            l = i+1
            r = n-1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            x = nums[i]
            while l < r:
                cSum = nums[r] + nums[l] + x
                if cSum < 0:
                    l += 1
                elif cSum > 0:
                    r -= 1
                else:
                    res.append([x, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return res
        
