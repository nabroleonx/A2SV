class Solution:
    def findComplement(self, num: int) -> int:
        x = 1
        
        while num >= x:
            x <<= 1
        
        res = (x-1)^num
        return res