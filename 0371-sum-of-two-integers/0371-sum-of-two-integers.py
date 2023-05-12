class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffff
        
        while(a & mask > 0):
            carry = (b & a) << 1
            b = b ^ a
            a = carry
        
        if a > 0:
            return b&mask
        else:
            return b