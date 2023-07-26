class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def fibonnaci(x):
            if x in cache:
                return cache[x]
            else:
                if x==0 or x==1:
                    return x
                else:
                    fib_x = fibonnaci(x-1) + fibonnaci(x-2)
                    cache[x] = fib_x
                    return fibonnaci(x)
            
        return fibonnaci(n)