class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:        
        n = len(events)
        
        events.sort(key=lambda x: x[1])
        
        max_sum = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(len(events)):
            event = events[i]
            start, end, value = event
            
            d = bisect_left(events, start, hi=i, key=lambda x: x[1])
            
            for j in range(1, k + 1):
                max_sum[i + 1][j] = max(max_sum[i][j], max_sum[d][j - 1] + value)
                
        return max_sum[n][k]
