class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        count = collections.Counter()
        
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            min_ = min(count['T'], count['F'])
            
            if min_ <= k:
                res += 1
            else:
                count[answerKey[right - res]] -= 1

        return res