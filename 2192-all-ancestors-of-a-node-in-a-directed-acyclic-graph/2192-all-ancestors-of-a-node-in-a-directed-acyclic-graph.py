class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        ancestors = defaultdict(list)
        
        for parent, child in edges:
            adj[parent].append(child)

        queue = deque()

        for node in range(n):
            queue.append((node, node))

        while queue:
            node, source = queue.popleft()

            for i in adj[node]:
                if source not in ancestors[i]:
                    ancestors[i].append(source)
                    queue.append((i, source))
                    
        return [sorted(ancestors[node]) for node in range(n)]
