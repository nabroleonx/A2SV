class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        res = 0
        sum_ = 0
        for i, j in nums:
            sum_ += j
            heappush(heap, j)
            if len(heap) == k:
                res = max(res, sum_ * i)
                sum_ -= heappop(heap)
        return res