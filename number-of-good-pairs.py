# Problem: https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = defaultdict(int)
        pairs = 0
        for i in nums:
            pairs += x[i]
            x[i] += 1
        return pairs
    
