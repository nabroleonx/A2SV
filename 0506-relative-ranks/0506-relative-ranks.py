class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [""] * len(score)
        scores = []
        for i, num in enumerate(score):
            scores.append((num, i))
        scores.sort(reverse=True)
        
        rankTitles = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        rank = 0
        
        for _, i in scores:
            if rank > 2:
                res[i] = str(rank + 1)
            else:
                res[i] = rankTitles[rank]
            rank += 1
        return res