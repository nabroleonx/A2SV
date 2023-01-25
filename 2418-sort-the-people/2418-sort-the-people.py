class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashMap = {k:v for k,v in zip(heights, names)}
        for i in range(len(heights)):
            for j in range(len(heights)-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        res = []
        for i in heights:
            res.append(hashMap[i])
        
        return res
    