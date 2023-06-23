class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        no_prerequisites = [i for i in range(numCourses) if indegree[i] == 0]
        
        queue = deque(no_prerequisites)
        
        courses_taken = 0
        while queue:
            x = queue.popleft()
            courses_taken += 1
            for i in adj[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        if courses_taken == numCourses:
            return True
        
        return False