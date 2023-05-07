class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        pt = 0
        j = 0
        
        if not s:
            return True
        
        while j < len(s):
            for i in range(pt, len(t)):
                if s[ps] == t[pt]:
                    ps += 1     
                if ps == len(s):
                    return True
                pt += 1
            j += 1

        return False
                    