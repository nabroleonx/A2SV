class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        left = 0
        right = n
        end = len(nums)
        while(left < n and right < end):
            res.append(nums[left])
            res.append(nums[right])
            left += 1
            right += 1
        return res