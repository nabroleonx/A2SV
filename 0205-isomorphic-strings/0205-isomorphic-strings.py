class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matchS = {}
        matchT = {}
        
        for i in range(len(s)):
            if (s[i] not in matchS) and (t[i] not in matchT):
                matchS[s[i]] = t[i]         
                matchT[t[i]] = s[i]
            
            elif matchS.get(s[i]) != t[i] or matchT.get(t[i]) != s[i]:
                return False
        
        return True
