#Problem: https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sum_so_far = 0
        noSubArr = 0
        values = defaultdict(int)
        values[0] = 1
        for i in range(len(nums)):
            sum_so_far += nums[i] % 2
            if sum_so_far - k in values:
                noSubArr += values[sum_so_far-k]
            values[sum_so_far] += 1
        return noSubArr
        
