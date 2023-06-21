class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        num_cost_pairs = sorted(zip(nums, cost))
        n = len(num_cost_pairs)
        prefix_cost_sum = [0] * (n + 1)
        suffix_cost_sum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            num, cost = num_cost_pairs[i - 1]
            prefix_cost_sum[i] = prefix_cost_sum[i - 1] + num * cost
            suffix_cost_sum[i] = suffix_cost_sum[i - 1] + cost
        
        min_total_cost = inf
        for i in range(1, n + 1):
            num = num_cost_pairs[i - 1][0]
            left_cost = num * suffix_cost_sum[i - 1] - prefix_cost_sum[i - 1]
            right_cost = prefix_cost_sum[n] - prefix_cost_sum[i] - num * (suffix_cost_sum[n] - suffix_cost_sum[i])
            total_cost = left_cost + right_cost
            min_total_cost = min(min_total_cost, total_cost)
        
        return min_total_cost