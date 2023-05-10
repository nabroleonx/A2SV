class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {}
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        def backtrack(curr, count):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in count:
                if count[i] > 0:
                    curr.append(i)
                    count[i] -= 1
                    backtrack(curr, count)
                    curr.pop()
                    count[i] += 1
        
        backtrack([], count)
        
        return res