class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m, n = len(mat), len(mat[0])
        visited = [[False]*n for _ in range(m)]
        res = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = True
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            i, j, d = queue.popleft()

            res[i][j] = d
            
            for dx, dy in directions:
                newx, newy = i+dx, j+dy
                
                if newx < 0 or newy < 0 or newx >= m or newy >= n or visited[newx][newy]:
                    continue
                
                queue.append((newx, newy, d+1))
                visited[newx][newy] = True
        
        return res
                    
            
        
                    
                
        
        
        