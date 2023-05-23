class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjecency_list = defaultdict(list)
        
        for i, j in edges:
            adjecency_list[i].append(j)
            adjecency_list[j].append(i)
        
        
        visited = set()
        queue = deque([source])
        
        
        while queue:
            cur = queue.popleft()
            
            if cur == destination:
                    return True
            
            for i in adjecency_list[cur]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                
        return False
        