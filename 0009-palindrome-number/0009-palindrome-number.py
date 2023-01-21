class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        temp = x
        res = 0
        while x > 0:
            lastDigit = x % 10
            res = res * 10 + lastDigit
            x = x // 10
        
        if temp == res:
            return True
        
        return False
            
