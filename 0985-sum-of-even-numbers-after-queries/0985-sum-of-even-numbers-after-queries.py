class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = sum([i for i in nums if i%2 == 0])
        for val, i in queries:
            if nums[i] % 2 == 0:
                even_sum -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                even_sum += nums[i]
            res.append(even_sum)
        return res
        