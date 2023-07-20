class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse=True)

        sum_, res = 0, 0
        
        res = 0
        for i in range(n):
            sum_ += satisfaction[i]
            if sum_ < 0:
                break
            res += sum_

        return res