# Problem: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    result = [0]*len(nums)
    index = 0
    for i in nums:
        for j in nums:
            if j < i:
                result[index] += 1
        index += 1
        
    return result
  
