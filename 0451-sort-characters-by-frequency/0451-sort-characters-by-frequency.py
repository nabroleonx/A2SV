class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        
        ss = [i for i in sorted(freq.items(), key=lambda x: x[1], reverse=True)]
        res = []
        
        for i in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            for _ in range(i[1]):
                res.append(i[0])
        
        return ''.join(res)
        
        