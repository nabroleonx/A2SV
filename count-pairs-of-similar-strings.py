# Problem: https://leetcode.com/problems/count-pairs-of-similar-strings

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashMap = {}
        pair = 0
        for i in words:
            x = ''.join(sorted(set(i)))
            pair += hashMap.get(x, 0)
            hashMap[x] = hashMap.get(x, 0) + 1
        return pair
                   
