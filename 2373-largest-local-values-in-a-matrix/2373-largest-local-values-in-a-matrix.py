class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid) - 3 + 1
        res = [[0] * m for _ in range(m)]
        for r in range(n - 2):
            for c in range(n - 2):
                matrix = [r[c:c+3] for r in grid[r:r+3]]
                res[r][c] = max([max(r) for r in matrix])
        return res