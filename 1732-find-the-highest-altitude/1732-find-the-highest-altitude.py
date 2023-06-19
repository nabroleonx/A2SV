class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = 0
        
        pref = 0
        
        for i in range(len(gain)):
            pref += gain[i]
            max_ = max(max_, pref)
        return max_