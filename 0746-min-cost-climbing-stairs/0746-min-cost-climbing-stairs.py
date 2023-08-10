class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1 = cost[0]
        cost2 = cost[1]
        
        for i in cost[2:]:
            cost1, cost2 = cost2, min(cost1, cost2) + i
        
        return min(cost1, cost2)