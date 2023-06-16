class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9+7
        
        leftChildsLen, rightChildsLen = 0, 0
        
        def comb(leftChildsLen, rightChildsLen):
            return factorial(leftChildsLen + rightChildsLen)//(factorial(leftChildsLen) * factorial(rightChildsLen))
        
        def dfs(bst):
            if len(bst) <= 2:
                return 1
            
            leftChilds = [num for num in bst if num < bst[0]]
            rightChilds = [num for num in bst if num > bst[0]] 

            return dfs(leftChilds) * dfs(rightChilds) * comb(len(leftChilds), len(rightChilds)) 
        
        ways = dfs(nums)
        
        return (ways - 1)%mod
        
        