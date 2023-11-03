class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p1 = p2 = 0
        
        if len(str2) > len(str1):
            return False
        
        while p1 < len(str1) and p2 < len(str2):
            next_char = chr(ord(str1[p1])+1) if str1[p1] != 'z' else 'a'
        
            if str2[p2] == str1[p1] or str2[p2] == next_char:
                p2 += 1
            
            p1 += 1
            
        if p2 != len(str2):
            return False
        else:
            return True