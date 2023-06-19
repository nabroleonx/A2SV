class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = 0
        
        pref = [0]
        
        for i in range(len(gain)):
            pref.append(gain[i] + pref[-1])
            max_ = max(max_, pref[-1])
        return max_