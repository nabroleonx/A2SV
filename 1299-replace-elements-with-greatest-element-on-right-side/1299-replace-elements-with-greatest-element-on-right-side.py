class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:   
        res = [0 for _ in arr]
        res[-1] = -1
        max_so_far = arr[-1]
        
        r = len(arr)-2 
        
        while r > -1:
            res[r] = max_so_far
            if arr[r] > max_so_far:
                max_so_far = arr[r]
            r -= 1
        return res