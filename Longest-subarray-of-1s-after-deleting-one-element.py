#Problem: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        zero_count = 1
        len_arr = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count-=1
            while i < len(nums) and zero_count < 0:
                if nums[i] == 0:
                    zero_count+=1
                i+=1
            len_arr = max(len_arr,j-i+1)
        return len_arr - 1
