class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        res = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            res[i] = stoneValue[i] - res[i + 1]
            if i + 2 <= n:
                res[i] = max(res[i], stoneValue[i] + stoneValue[i + 1] - res[i + 2])
            if i + 3 <= n:
                res[i] = max(res[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - res[i + 3])
                
        if res[0] > 0:
            return "Alice"
        if res[0] < 0:
            return "Bob"
        return "Tie"