class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        elapsed_time = 0
        row, col = len(grid), len(grid[0])
        fresh = 0
        rotten = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j])

        while queue and fresh > 0:          
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for i, j in directions:
                    x = r + i
                    y = c + j

                    if x < 0 or y < 0 or x == row or y == col or grid[x][y] != 1:
                        continue
                    grid[x][y] = 2
                    queue.append([x,y])
                    fresh -= 1
            elapsed_time += 1
    
        if fresh != 0:
            return -1
        
        return elapsed_time