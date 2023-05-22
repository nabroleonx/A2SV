class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq  = {}
        
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        res = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        return [i[0] for i in res[:k]]
        
        