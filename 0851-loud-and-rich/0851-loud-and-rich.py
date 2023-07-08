class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        '''
        1 -> 0
        2 -> 1
        4 -> 3 -> 7/1
        5 -> 3 -> 1 -> 0
        6 -> 3
        '''
        n = len(quiet)
        adj = defaultdict(list)
        indegree = [0 for _ in range(n)]
        res = [i for i in range(n)]
        
        for a, b in richer:
            adj[a].append(b)
            indegree[b] += 1
        
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            i = queue.popleft()
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
                if quiet[res[i]] < quiet[res[j]]:
                    res[j] = res[i]
        return res
            