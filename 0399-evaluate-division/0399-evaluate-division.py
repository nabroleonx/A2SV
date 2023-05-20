class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            u, v = equations[i]
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
        
        def dfs(start, end, visited):
            if start in visited or start not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor, value in graph[start].items():
                path_value = dfs(neighbor, end, visited)
                
                if path_value != -1.0:
                    return value * path_value
                
            return -1.0
        
        result = []
        for query in queries:
            start, end = query

            result.append(dfs(start, end, set()))
        
        return result