class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        
        if n == 1:
            return [0]
        
        if n == 2:
            return [0, 1]
        
        adj = defaultdict(list)
        degree = [0] * n
        res = []
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        leaves = [i for i in range(n) if degree[i] == 1]
        queue = deque(leaves)

        while queue:
            temp = []
            cur_len = len(queue)
            
            while cur_len > 0:
                i = queue.popleft()
                temp.append(i)
                
                for j in adj[i]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        queue.append(j)
                
                cur_len -= 1
            
            res = temp
        
        return res