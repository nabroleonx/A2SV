class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        
        for r in ransomNote:
            ransom[r] = ransom.get(r, 0) + 1
        
        for m in magazine:
            if m in ransom:
                ransom[m] -= 1
                
                if ransom[m] == 0:
                    del ransom[m]
        
        return True if not ransom else False