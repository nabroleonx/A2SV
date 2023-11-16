class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        
        def bfs(queue, visited):
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for x, y in directions:
                        newx, newy = i + x, j + y
                        
                        if (newx >= 0 and newx < row 
                            and newy >= 0 and newy < col 
                            and (newx, newy) not in visited 
                            and heights[newx][newy] >= heights[i][j]
                           ):
                            queue.append((newx, newy))
                            visited.add((newx, newy))
                            
        row = len(heights)
        col = len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    pacific_queue.append((i, j))
                    pacific.add((i, j))
                if i == row - 1 or j == col - 1:
                    atlantic_queue.append((i, j))
                    atlantic.add((i, j))
        
        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)
        
        res = []
        
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append((i, j))
        
        return res