class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        def count(mid):
            i, count = 0, 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count
        
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = l + (r - l) // 2

            if count(mid) >= p:
                r = mid
            else:
                l = mid + 1
        return l 