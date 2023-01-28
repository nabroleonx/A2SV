class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = []
        l = 0
        r = len(piles)-1
        while l < r:
            res.append(piles[r])
            res.append(piles[r-1])
            res.append(piles[l])
            l += 1
            r -= 2
        max_coins = 0
        i = 1
        while i < len(res):
            max_coins += res[i]
            i+=3
        return max_coins
            