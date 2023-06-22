class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        max_profit = 0
        buying_price = prices[0]
        for price in prices:
            if price < buying_price:
                buying_price = price
            if price > buying_price + fee:
                max_profit += price - buying_price - fee
                buying_price = price - fee
        
        return max_profit