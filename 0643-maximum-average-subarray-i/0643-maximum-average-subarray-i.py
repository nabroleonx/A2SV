class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k-1
        cur_sum = sum(nums[l:r+1])
        res = cur_sum
        while r < len(nums)-1:
            cur_sum -= nums[l]
            l += 1

            r += 1
            cur_sum += nums[r]

            res = max(res, cur_sum)
        return res/k   
            