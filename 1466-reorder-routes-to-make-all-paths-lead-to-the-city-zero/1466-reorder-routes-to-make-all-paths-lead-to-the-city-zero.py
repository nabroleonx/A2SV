class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        reorder = 0
        edges = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            edges.add((a, b))
    
        def dfs(city):
            nonlocal reorder

            if city not in visited:
                visited.add(city)
                for neighbor in graph[city]:
                    if neighbor not in visited:
                        if (neighbor, city) not in edges:
                            reorder += 1
                        dfs(neighbor)

        dfs(0)

        return reorder
