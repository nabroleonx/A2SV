class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0 for _ in range(n)]
        adj = defaultdict(list)
        
        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
                indegree[i] += 1
                
        terminal = [i for i in range(n) if indegree[i] == 0]
            
        queue = deque(terminal)
        
        safe_nodes = set()
        
        while queue:
            x = queue.popleft()
            
            safe_nodes.add(x)
            
            for i in adj[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            
        return sorted(list(safe_nodes))
                