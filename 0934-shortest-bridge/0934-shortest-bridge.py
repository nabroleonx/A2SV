class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        
        def dfs(i, j):
            if i < 0 or j < 0 or i == n or j == n or (i, j) in visited or not grid[i][j]:
                return
            visited.add((i, j))
            for r, c in directions:
                dfs(i+r, j+c)
        
        def bfs():
            queue = deque(visited)
            flipped = 0
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    
                    for r, c in directions:
                        row, col = i+r, j+c
                        if row < 0 or col < 0 or row == n or col == n or (row, col) in visited:
                            continue
                        if grid[row][col]:
                            return flipped
                        
                        queue.append((row, col))
                        visited.add((row, col))
                flipped += 1
                
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs()
                    
                    