class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr = [-1] + arr + [-1]
        res = 0
        
        n = len(arr)
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                res += arr[j] * (i-j) * (j-stack[-1])
            
            stack.append(i)
            
        return res % (10**9 + 7)
            
        