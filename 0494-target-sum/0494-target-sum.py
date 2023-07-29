class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        
        if sum_ < target or (sum_ - target) % 2 != 0:
            return 0
        
        n = (sum_ - target) // 2
        
        dp = [0] * (n + 1)
        
        dp[0] = 1
        
        for i in nums:
            for j in range(n, i - 1, -1):
                dp[j] += dp[j - i]
        return dp[-1]