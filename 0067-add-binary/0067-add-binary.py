class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        
        while b > 0:
            carry = (a&b)<<1
            a = a ^ b
            b = carry
        
        return str(bin(a)[2:])