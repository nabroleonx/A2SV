class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num_subsets = 2**len(nums)
        res = []
        
        for i in range(num_subsets):
            subset = []
            
            for j in nums:
                if i % 2 == 1:
                    subset.append(j)
                i = i // 2
            res.append(subset)
        
        return res