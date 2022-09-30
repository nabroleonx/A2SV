#Problem: https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        newArray = []
        
        left_ptr, right_ptr = 0, len(nums)-1
        while len(newArray) != len(nums):
            newArray.append(nums[left_ptr])    
            left_ptr+=1
            
            if left_ptr <= right_ptr:
                newArray.append(nums[right_ptr])
                right_ptr-=1
            
        return newArray
        
