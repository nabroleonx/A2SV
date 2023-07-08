class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if n == k or k == 1:
            return 0

        score = []
        for i in range(n-1):
            score.append(weights[i]+weights[i+1] )
            
        score.sort()

        return sum(score[-(k-1):]) - sum(score[:k-1])