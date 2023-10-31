class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        res = [1]
        
        for i in nums[:-1]:
            pre *= i
            res.append(pre)
            
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
            
        return res
    