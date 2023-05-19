class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph) 
        colors = [None] * n 
        
        for i in range(n): 
            if colors[i] is not None: 
                continue 
                
            colors[i] = True 
            stack = [i] 
            
            while stack: 
                node = stack.pop() 
                
                for j in graph[node]: 
                    if colors[j] is None: 
                        colors[j] = not colors[node]           
                        stack.append(j) 
                        
                    elif colors[j] == colors[node]: 
                        return False 
        return True