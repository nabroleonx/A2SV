class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        while n >= 1:
            n /= 4
            if n == 1:
                return True
        return False
