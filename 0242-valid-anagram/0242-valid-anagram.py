class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        
        if len(s) != len(t):
            return False
        
        for i in s:
            freq[i] = freq.get(i, 0) + 1
            
        for i in t:
            if i in freq:
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
        
        return True if not freq else False