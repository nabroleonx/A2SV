class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True for _ in range(n+1)]
        
        is_prime[0] = False
        is_prime[1] = False
        
        i = 2
        res = n-2
        for i in range(2, int(math.sqrt(n))+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    if is_prime[j]:
                        res -= 1
                    is_prime[j] = False
            i += 1
        
        return res