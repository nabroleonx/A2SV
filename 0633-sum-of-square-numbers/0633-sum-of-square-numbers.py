class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # n = c**(1/2)
        # l, r = 0, int(n)         
        # while l <= r:
        #     if l**2 + r**2 == c:
        #         print(r, l)
        #         return True
        #     elif l**2 + r**2 < c:
        #         l += 1
        #     else:
        #         r -= 1
        # return False

        if c == 0:
            return True
        if c == 2:
            return True
        
        for i in range(floor(c ** 0.5)+1):
            rem = c - (i * i)
            if rem == (floor(rem ** 0.5)) ** 2:
                return True
        return False