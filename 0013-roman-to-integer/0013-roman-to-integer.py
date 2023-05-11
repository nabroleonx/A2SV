class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        res = 0
        i = len(s)-1
        while i > -1:
            if i > 0 and roman[s[i-1]] < roman[s[i]]:
                res += roman[s[i]]-roman[s[i-1]]
                i -= 2
                continue

            res += roman[s[i]]
            i -= 1
        
        return res
            
            