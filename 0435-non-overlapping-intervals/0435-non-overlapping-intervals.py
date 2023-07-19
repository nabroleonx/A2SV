class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        
        removed = 0
        left = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < left[1]:
                removed += 1
            else:
                left = intervals[i]
        return removed