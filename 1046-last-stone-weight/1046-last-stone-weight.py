class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * i for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            
            if x == y:
                continue
            else:
                x = x - y
                heapq.heappush(stones, -x)
        
        return -heapq.heappop(stones) if len(stones) > 0 else 0
        