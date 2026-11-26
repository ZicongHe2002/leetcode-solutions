from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals):
        ordered = sorted((start, index) for index, (start, _) in enumerate(intervals))
        starts = [start for start, _ in ordered]
        result = []
        for _, end in intervals:
            position = bisect_left(starts, end)
            result.append(ordered[position][1] if position < len(ordered) else -1)
        return result
