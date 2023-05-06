class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):  
            if n<=2:
                return []
            is_prime = [True]*(n)
            is_prime[0] = False
            is_prime[1] = False
            
            for i in range(2, int(math.sqrt(n))+1):
                if is_prime[i]:
                    for j in range(i*i, n, i):
                        is_prime[j] = False
                        
            # return [i for i in range(left, right) if is_prime[i]]
            return [i for i in range(n) if is_prime[i]]
            
        primes = sieve(right+1)
        # print(primes)
        
        min_diff = float('inf')
        res = [-1, -1]
        
        for i in range(1, len(primes)):
            if primes[i]>=left and primes[i-1]>=left and primes[i] - primes[i-1] < min_diff:
                res = [primes[i-1], primes[i]]
                min_diff = primes[i] - primes[i-1]
                
        return res
            