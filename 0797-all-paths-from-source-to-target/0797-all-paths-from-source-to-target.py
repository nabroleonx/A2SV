class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = set()
        paths = []
        
        def dfs(paths, i, path):
            if i == n - 1:
                paths.append(path)
                return
            else:
                for j in graph[i]:
                    dfs(paths, j, path + [j])
        
        dfs(paths, 0, [0])
        
        return paths