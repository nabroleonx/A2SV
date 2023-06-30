class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def good(days):
            lands = [[0] * col for _ in range(row)]
            
            for i in range(days):
                x, y = cells[i]
                lands[x - 1][y - 1] = 1
            
            queue = deque()
            for y in range(col):
                if lands[0][y] == 0:
                    queue.append((0, y))
                    lands[0][y] = 1
            
            while queue:
                x, y = queue.popleft()
                if x == row - 1: 
                    return True

                for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= dx < row and 0 <= dy < col and lands[dx][dy] == 0:
                        queue.append((dx, dy))
                        lands[dx][dy] = 1
            
            return False
        
        l, r = 1, len(cells)
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            if good(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
                
        return res