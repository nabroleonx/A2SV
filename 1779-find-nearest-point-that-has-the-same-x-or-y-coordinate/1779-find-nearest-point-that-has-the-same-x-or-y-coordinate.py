class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis = float('inf')
        res = -1
        for i,p in enumerate(points):
            if x == p[0] or y == p[1]:
                dis = abs(x-p[0]) + abs(y-p[1])
                if dis < min_dis:
                    min_dis = dis
                    res = i
        return res
