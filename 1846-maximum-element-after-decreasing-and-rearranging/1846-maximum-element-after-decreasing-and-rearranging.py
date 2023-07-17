class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        max_val = float('-inf')
        
        for i in range(len(arr)):
            arr[i] = min(arr[i - 1] + 1, arr[i])
            max_val = max(max_val, arr[i])
        
        return max_val

            