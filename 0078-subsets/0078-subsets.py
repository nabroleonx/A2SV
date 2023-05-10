class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        def backtrack(res, curr, start):
            res.append(curr.copy())
            
            for i in range(start, len(nums)):
                # print(f'cur: {curr}, start: {start}, res: {res}')
                curr.append(nums[i])
                backtrack(res, curr, i+1)
                curr.pop()
        
        backtrack(res, [], 0)
        
        return res