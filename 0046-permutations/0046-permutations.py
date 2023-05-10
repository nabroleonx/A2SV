class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = {i: False for i in range(len(nums))}
        
        
        
        def backtrack(res, curr, nums, visited):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                curr.append(nums[i])
                visited[i] = True
                backtrack(res, curr, nums, visited)
                curr.pop()
                visited[i] = False
        
        backtrack(res, [], nums, visited)
        
        return res
        