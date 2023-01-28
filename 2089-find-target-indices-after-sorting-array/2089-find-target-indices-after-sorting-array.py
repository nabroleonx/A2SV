class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, 0
        if target in nums:
            for i in range(len(nums)):
                if target > nums[i]:
                    l += 1
                elif target == nums[i]:
                    r += 1
            return [i for i in range(l, l+r)]
        return []
                