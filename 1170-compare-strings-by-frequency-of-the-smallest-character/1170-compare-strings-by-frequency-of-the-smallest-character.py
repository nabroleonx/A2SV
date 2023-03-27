class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        n = len(words)
        def f(s):            
            x = min(set(s))
            return s.count(x)
        
        def less_frequent_BS(q):
            l = 0
            r = n-1
            pos = -1
            while l<=r:
                mid = (l+r)//2
                if words[mid] <= q:
                    l = mid + 1
                elif words[mid] > q:
                    pos = mid
                    r = mid - 1
                    
            return n-pos if pos != -1 else 0 
 
        queries = [f(q) for q in queries]
        words = [f(w) for w in words]
        
        words.sort()
        
        res = []
        for q in queries:
            lf = less_frequent_BS(q)
            res.append(lf)
            
        return res