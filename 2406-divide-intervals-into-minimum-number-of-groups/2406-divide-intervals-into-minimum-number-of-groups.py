class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        '''
        intervals.sort()
        heap = []
        
        for interval in intervals:
            start, end = interval
            
            if heap and heap[0] < start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)
        '''
        # alternative solution using prefix sum
        max_end = 10**6 + 2
        count = [0 for _ in range(max_end)]
        
        for interval in intervals:
            start, end = interval
            
            count[start] += 1
            count[end+1] -= 1
        
        groups = float('-inf')
        
        for i in range(1, len(count)):
            count[i] += count[i-1]
            groups = max(groups, count[i])
            
        return groups