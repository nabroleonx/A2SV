class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            count += 1
        
        for col in range(1, n):
            for row in range(col):
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    count += 1
                    
                elif s[col] == s[row] and dp[row + 1][col - 1]:
                    dp[row][col] = 1
                    count += 1
        return count
