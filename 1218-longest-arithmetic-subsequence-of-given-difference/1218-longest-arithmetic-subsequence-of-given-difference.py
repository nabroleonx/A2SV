class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        subsequences = defaultdict(int)
        
        for i in arr:
            subsequences[i] = subsequences[i-difference] + 1
        
        # print(subsequences)
        return max(subsequences.values())