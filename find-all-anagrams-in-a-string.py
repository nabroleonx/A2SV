# Problem: https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = defaultdict(int)
        sCount = defaultdict(int)
        
        if len(p) > len(s):
            return []
        
        for i, val in enumerate(p):
            pCount[val] += 1
            sCount[s[i]] += 1
        
        res = []
        left = 0   
        if sCount == pCount:
            res.append(0)
        
        for right in range(len(p), len(s)):
            sCount[s[right]] += 1
            sCount[s[left]] -= 1
            
            if sCount[s[left]] == 0:
                del sCount[s[left]]
            left+=1
            if sCount == pCount:
                res.append(left)
        return res
            
