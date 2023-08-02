class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [n] * n
        dp[0] = 0
        
        for coin in coins:
            for j in range(coin, n):
                dp[j] = min(dp[j], dp[j - coin] + 1)
                
        return -1 if dp[-1] > amount else dp[-1]