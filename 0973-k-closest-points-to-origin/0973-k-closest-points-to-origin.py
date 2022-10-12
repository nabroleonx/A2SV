class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        resHeap = []
        for i in range(len(points)):
            x, y = points[i]
            d = (x**2 + y**2)
            resHeap.append([d, x, y])
        result = []
        heapq.heapify(resHeap)
        while k > 0:
            result.append(heapq.heappop(resHeap)[1:])
            k -= 1
        return result
        
        