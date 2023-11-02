class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(a,b):
            if b in adj[a]:
                return True
            
            if (a, b) in memo:
                return memo[(a, b)]
            
            for pr in adj[a]:
                if dfs(pr, b):
                    memo[(a,b)] = True
                    return True
                
            memo[(a,b)] = False
            return False
            
        memo = {}
        
        adj = defaultdict(set)
        for a, b in prerequisites:
            adj[a].add(b)
            
        res = []
        
        for a, b in queries:
            res.append(dfs(a, b))
        
        return res