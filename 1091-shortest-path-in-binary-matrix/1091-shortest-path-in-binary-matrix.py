class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        queue.append((0,0,1))
        visited.add((0,0))
        n = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
        if grid[0][0] == 1:
            return -1

        while queue:
            for _ in range(len(queue)):
                i, j, res = queue.popleft()

                if i == n-1 and j == n-1:
                    return res

                for r, c in directions:
                    curR, curC = i + r, j + c

                    if curR < 0 or curC < 0 or curR >= n or curC >= n or grid[curR][curC] == 1 or (curR, curC) in visited:
                        continue

                    queue.append((curR, curC, res+1))
                    visited.add((curR, curC))
        
        return -1