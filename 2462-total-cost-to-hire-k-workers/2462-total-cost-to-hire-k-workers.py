class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        first = candidates - 1
        last = n - candidates
        
        workersCost = []
        
        for i in range(candidates):
            heapq.heappush(workersCost, (costs[i], i))
        
        for i in range(n-candidates, n):
            if i <= first:
                continue
            heapq.heappush(workersCost, (costs[i], i))
        
        totalCost = 0
        
        while k > 0:
            cost, i = heapq.heappop(workersCost)
            
            totalCost += cost
            
            if i >= last:
                last -= 1
                if last > first:
                    heapq.heappush(workersCost, (costs[last], last))
            
            if i <= first:
                first += 1
                if first < last:
                    heapq.heappush(workersCost, (costs[first], first))
            
            k -= 1
            
        return totalCost