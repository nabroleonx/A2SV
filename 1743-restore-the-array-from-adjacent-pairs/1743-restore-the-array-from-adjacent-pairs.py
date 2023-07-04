class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res = []
        adj = defaultdict(list)
        
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        
        for node in adj:
            if len(adj[node]) == 1:
                res.append(node)
                res.append(adj[node][0])
                break
        
        while len(res) < len(adjacentPairs) + 1:
            last_node, prev = res[-1], res[len(res)-2]
            
            node = adj[last_node]
            
            if node[0] == prev:
                res.append(node[1])
            else:
                res.append(node[0])
        
        return res