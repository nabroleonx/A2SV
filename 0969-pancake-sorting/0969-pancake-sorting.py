class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def findmax(x):
            maxI = x
            for i in range(x, -1, -1):
                if arr[i] > arr[maxI]:
                    maxI = i
            return maxI
        
        def reverse(r):
            l = 0
            while l < r:
                arr[r], arr[l] = arr[l], arr[r]
                l+=1
                r-=1
                
        res = []
        for i in range(len(arr)-1, -1, -1):
            maxI = findmax(i)
            if maxI != i:
                reverse(maxI)
                reverse(i)
                res.append(maxI+1)
                res.append(i+1)
        return res
                