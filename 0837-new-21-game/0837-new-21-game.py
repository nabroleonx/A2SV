class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        res = [0] * (n + 1)
        res[0] = 1

        if k > 0:
            s = 1
        else:
            s = 0
            
        for i in range(1, n + 1):
            res[i] = s / maxPts
            if i < k:
                s += res[i]
            if i - maxPts >= 0:
                if i - maxPts < k:
                    s -= res[i - maxPts]
        return sum(res[k:])