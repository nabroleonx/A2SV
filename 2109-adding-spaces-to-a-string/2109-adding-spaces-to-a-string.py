class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        ptr = 0
        for i in range(len(s)):
            if ptr < len(spaces) and i == spaces[ptr]:
                res += ' '
                res += s[i]
                ptr += 1
            else:
                res += s[i]
        
        return res
            
