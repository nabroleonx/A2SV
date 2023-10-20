class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + cardPoints[i]
            
        max_points = float('inf')
        for i in range(n):
            j = i + (n - k) - 1
            if j < n:
                max_points = min(max_points, pref[j + 1] - pref[i])
                
        return pref[-1] - max_points