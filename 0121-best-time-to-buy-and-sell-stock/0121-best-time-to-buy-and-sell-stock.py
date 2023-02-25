class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        n = len(prices)
        for r in range(n):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r]-prices[l])
            else:
                l = r
        return profit
        