class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num == '.':
                    continue
                
                grid = 3*(r//3) + c//3
                if num in rows[r] or num in cols[c] or num in grids[grid]:
                    return False
    
                rows[r].add(num)             
                cols[c].add(num)
                grids[grid].add(num)
        return True