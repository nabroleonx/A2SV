class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        row, col = len(maze), len(maze[0])
        visited = [[False]*col for _ in range(row)]
        
        x, y = entrance
        
        queue.append((x, y, 0))
        visited[x][y] = True
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while queue:
            i, j, d = queue.popleft()
            
            if i == row-1 or j == col-1 or i == 0 or j == 0:
                if i != x or j != y:
                    return d
            
            for dx, dy in directions:
                newx, newy = dx + i, dy + j
                
                if newx < 0 or newy < 0 or newx >= row or newy >= col or maze[newx][newy] == "+" or visited[newx][newy]:
                    continue
                
                queue.append((newx, newy, d+1))

                visited[newx][newy] = True
        
        return -1
            
            
            