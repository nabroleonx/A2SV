class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(n, requests, idx, transfers):
            if idx == len(requests):
                for i in range(n):
                    if transfers[i] != 0:
                        return float('-inf')
                return 0

            i, j = requests[idx]
            transfers[i] -= 1
            transfers[j] += 1
            
            take = backtrack(n, requests, idx + 1, transfers)
            
            transfers[i] += 1
            transfers[j] -= 1

            skip = backtrack(n, requests, idx + 1, transfers)

            return max(take + 1, skip)
        
        return backtrack(n, requests, 0, [0] * n)
