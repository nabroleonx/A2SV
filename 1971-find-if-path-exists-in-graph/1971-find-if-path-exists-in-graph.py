class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjecency_list = defaultdict(list)
        
        for i, j in edges:
            adjecency_list[i].append(j)
            adjecency_list[j].append(i)
        
        
        visited = set()
        
        def dfs(i):
            if i == destination:
                return True
            
            if i not in visited:
                visited.add(i)
                
                for j in adjecency_list[i]:
                    if dfs(j):
                        return True
            
            return False
        
        return dfs(source)