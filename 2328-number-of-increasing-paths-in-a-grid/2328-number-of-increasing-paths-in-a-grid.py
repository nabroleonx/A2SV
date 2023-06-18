class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        modulo = 10**9 + 7
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        total_paths = 0

        @cache
        def dfs(row, col):
            count = 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] > grid[row][col]:
                    count += dfs(new_row, new_col)
            return count

        for row in range(rows):
            for col in range(cols):
                total_paths += dfs(row, col)
                total_paths %= modulo

        return total_paths
