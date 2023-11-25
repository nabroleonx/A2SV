class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sum_ = sum(nums)
        n = len(nums)
        res = []
        leftSum = 0
        
        for i in range(n):
            rightSum = sum_ - leftSum - nums[i]
            
            leftCount = i
            rightCount = n - i - 1
            
            leftDiff = nums[i] * leftCount - leftSum
            rightDiff = rightSum - nums[i] * rightCount
            
            res.append(leftDiff + rightDiff)
            leftSum += nums[i]
        
        return res