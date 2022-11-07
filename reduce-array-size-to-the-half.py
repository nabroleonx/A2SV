# Problem: https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = {}
        n = len(arr)
        for i in arr:
            count[i] = 1 + count.get(i, 0)
        freq_list = list(count.values())
        freq_list.sort()
        res = 0
        removed = 0
        while removed < n//2:
            removed += freq_list.pop()
            res += 1
        return res
        
