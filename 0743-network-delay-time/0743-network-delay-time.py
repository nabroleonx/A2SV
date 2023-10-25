class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)
        for u, v, w in times:
            network[u - 1].append((v - 1, w))
            
        delay = [float('inf') for _ in range(n)]
        delay[k - 1] = 0
        
        queue = [(0, k - 1)]
        
        while queue:
            _, u = heappop(queue)
            for v, w in network[u]:
                if delay[v] > delay[u] + w:
                    delay[v] = delay[u] + w
                    heappush(queue, (delay[v], v))
                    
        res = max(delay)
        
        return -1 if res == float('inf') else res
