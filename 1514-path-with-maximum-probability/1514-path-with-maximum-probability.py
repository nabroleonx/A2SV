class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        for (a, b), s in zip(edges, succProb):
            adj[a].append((b, s))
            adj[b].append((a, s))
            
        heap = [(-1, start)]
        prob = [0] * n
        prob[start] = 1
        
        while heap:
            weight, a = heapq.heappop(heap)
            weight = -weight
            if prob[a] > weight:
                continue
            for b, s in adj[a]:
                if prob[b] < prob[a] * s:
                    prob[b] = prob[a] * s
                    heapq.heappush(heap, (-prob[b], b))
                    
        return prob[end]