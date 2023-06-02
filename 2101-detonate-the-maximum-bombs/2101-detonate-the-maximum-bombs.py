class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        edge = defaultdict(list)
        def euclid(b1, b2):
            a, b, c = b1
            x, y, z = b2
            
            dist = math.sqrt((x-a)**2 + (y-b)**2)
            
            return dist <= c
        
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if euclid(bombs[i], bombs[j]):
                    edge[i].append(j)
                    
        def dfs(i, visited):
            if i in visited:
                return 0
            cur = 1
            visited.add(i)
            for j in edge[i]:
                cur += dfs(j, visited)
            
            return cur
        
        ans = 0
        for i in range(n):
            visited = set()
            if i not in visited:
                ans = max(ans, dfs(i, visited))
        
        return ans