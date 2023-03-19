class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for p in piles:
                totalTime += -1*(-1*p // mid)
            if totalTime <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res





