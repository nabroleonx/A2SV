class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        res = [0]*n
    
        for start, end, direction in shifts:
            if direction == 1:
                res[start] += 1
                if end + 1 < n:
                    res[end+1] -= 1
                    
            elif direction == 0:
                res[start] -= 1
                
                if end +1 < n:
                    res[end+1] += 1
        
        prefix = [0]
        for i in res:
            prefix.append(prefix[-1]+i)
            
        shifted = []
        for i in range(1, len(prefix)):
            shifted.append(chr(((ord(s[i-1])-97+prefix[i])%26) + 97))
        
        return ''.join(shifted)