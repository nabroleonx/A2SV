class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n

        for i in range(n):
            j = i + 1

            if i > 0 and nums[i] == nums[i - 1]:
                dp[j] |= dp[j - 2]
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                dp[j] |= dp[j - 3]
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                dp[j] |= dp[j - 3]
 
        return dp[n]