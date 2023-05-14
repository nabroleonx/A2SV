class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        c = 0
        count = Counter(nums)
        
        for i in count:
            if c < count[i]:
                res = i
                c = count[i]
        return res
    