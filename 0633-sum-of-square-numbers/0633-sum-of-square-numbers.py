class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = c**(1/2)
        l, r = 0, int(n)         
        while l <= r:
            if l**2 + r**2 == c:
                return True
            elif l**2 + r**2 < c:
                l += 1
            else:
                r -= 1
        return False
            