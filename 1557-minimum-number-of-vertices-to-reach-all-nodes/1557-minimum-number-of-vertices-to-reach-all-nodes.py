class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = set()
        destinations = set()
        
        for i, j in edges:
            sources.add(i)
            destinations.add(j)
        
        res = []
        for i in sources:
            if i not in destinations:
                res.append(i)
        
        return res