class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj = defaultdict(list)
        
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        independent = [i for i in range(numCourses) if indegree[i] == 0]
        
        queue = deque(independent)
        
        courses_taken = 0
        
        while queue:
            course = queue.popleft()
            courses_taken += 1
            
            for i in adj[course]:
                indegree[i] -= 1
                
                if indegree[i] == 0:
                    queue.append(i)
                    
        
        if courses_taken == numCourses:
            return True
        return False