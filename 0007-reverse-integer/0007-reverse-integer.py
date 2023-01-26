class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        if x > 2**31:
            return 0
        while x > 0:
            rem = x % 10
            rev = rev*10 + rem
            if rev > 2**31:
                return 0
            x = x//10
        return -1 * rev if neg else rev
        