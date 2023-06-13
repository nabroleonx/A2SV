class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0     
        pairs = {}
 
        for i in grid:
            pairs[tuple(i)] = pairs.get(tuple(i), 0) + 1
            
        for i in range(n):
            pair = []
            for j in range(n):
                pair.append(grid[j][i])
            
            if tuple(pair) in pairs:
                res += pairs[tuple(pair)]
            
        return res