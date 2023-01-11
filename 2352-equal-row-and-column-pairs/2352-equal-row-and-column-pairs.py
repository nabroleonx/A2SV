class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        hashMap = {}
        for row in grid:
            hashMap[tuple(row)] = hashMap.get(tuple(row), 0) + 1
        for column in range(len(grid)):
            columns = []
            for row in range(len(grid)):
                columns.append(grid[row][column])
            columns = tuple(columns)
            if columns in hashMap:
                res += hashMap[columns]
        return res
