class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        
        heap = []
        
        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                _, dest = heapq.heappop(heap)
                capacity += dest
            
            heapq.heappush(heap, (trip[2], trip[0]))
            capacity -= trip[0]
            
            if capacity < 0:
                return False
        
        return True