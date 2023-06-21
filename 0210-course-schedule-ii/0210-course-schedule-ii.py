class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
        adj = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        independent = [i for i in range(numCourses) if indegree[i] == 0]
        queue = deque(independent)
        
        res = []
        while queue:
            i = queue.popleft()
            res.append(i)
            
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        
        if len(res) == numCourses:
            return res
        
        return []