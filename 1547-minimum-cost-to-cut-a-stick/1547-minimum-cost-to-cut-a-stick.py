class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def helper(cuts, start, end, res):
            if start + 1 == end:
                return 0

            if res[start][end] != -1:
                return res[start][end]

            ans = float('inf')
            for i in range(start + 1, end):
                ans = min(ans, cuts[end] - cuts[start] + helper(cuts, start, i, res) + helper(cuts, i, end, res))
            res[start][end] = ans
            return res[start][end]


        
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        res = [[-1] * (len(cuts)) for _ in range(len(cuts))]
        return helper(cuts, 0, len(cuts) - 1, res)
    
