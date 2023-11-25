class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        prod = 1
        left = 0
        count = 0
        
        for right, val in enumerate(nums):
            prod *= val
            
            while prod >= k:
                prod /= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
            
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        n = len(nums)
        prod = 1
        count = 0
        
        while r < n:
            prod *= nums[r] 
            
            if prod < k:
                count += 1
                r += 1
            else:
                while prod >= k:
                    if nums[l] < k:
                        count += 1
                    prod /= nums[l]
                    l += 1
                count += 1
            

            '''
        