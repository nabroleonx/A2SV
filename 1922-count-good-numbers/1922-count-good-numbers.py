class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        no_evens = int(n // 2 + int(n % 2 != 0))
        no_odds = int(n // 2)
        
        def power(b, e):
            if e == 0: 
                return 1
            
            res = power(b, e // 2)
            
            if e % 2 == 0:
                return (res * res) % mod
            else:
                return (res * res * b) % mod
        
        
        
        return (power(5, no_evens) * power(4, no_odds)) % mod