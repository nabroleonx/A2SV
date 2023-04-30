class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        W = len(word)
        
        def dfs(i, j, w):
            if w == W:
                return True
            
            if (not 0 <= i < m or
                not 0 <= j < n or
                board[i][j] == '#' or
                board[i][j] != word[w]):
                return False
            
            curr_letter = board[i][j]
            board[i][j] = ''
            
            top = dfs(i - 1, j, w + 1)
            bottom = dfs(i + 1, j, w + 1)
            left = dfs(i, j - 1, w + 1)
            right = dfs(i, j + 1, w + 1)
            
            board[i][j] = curr_letter
            
            return top or bottom or left or right
        
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False