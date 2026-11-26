class Solution:
    def eraseOverlapIntervals(self, intervals):
        kept = 0
        previous_end = None
        for start, end in sorted(intervals, key=lambda interval: interval[1]):
            if previous_end is None or start >= previous_end:
                kept += 1
                previous_end = end
        return len(intervals) - kept
