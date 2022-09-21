# Problem: https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = 0
        prefixSumList = []
        
        for i in nums:
            prefixSum += i
            prefixSumList.append(prefixSum)
        
        for i in range(len(prefixSumList)):
            rightSum = prefixSumList[-1] - prefixSumList[i]
            leftSum = prefixSumList[i-1] if i > 0 else 0
            
            if(leftSum == rightSum):
                return i

        return -1
