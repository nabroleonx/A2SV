# Problem: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res =0
        count = 0
        for i in range(len(s)):
            if count == k:
                return k
            if s[i] in 'aeiou':
                count += 1
            if i >= k and s[i-k] in 'aeiou':
                count -= 1
            res = max(res, count)
        return res
                
