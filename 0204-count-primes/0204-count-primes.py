class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True]*n
        
        is_prime[0] = False
        is_prime[1] = False
        
        i = 2
        # res = n-2
        
        for i in range(2, int(math.sqrt(n))+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
                    # res -= 1
        
        return sum(is_prime)