class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        max_len = 1
        l, r = 0, 1

        while r < len(nums):
            if nums[r] - nums[l] <= 2 * k:
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                l += 1

        return max_len