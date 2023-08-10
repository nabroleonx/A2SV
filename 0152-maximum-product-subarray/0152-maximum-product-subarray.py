class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn = 1
        maxx = 1
        res = float('-inf')
        
        for num in nums:
            if minn == 0:
                minn = 1
            if maxx == 0:
                maxx = 1
                
            curMax = maxx
            maxx = max(num*maxx, num*minn, num)
            minn = min(num*minn, num*curMax, num)
            
            res = max(maxx, res)
        
        return res