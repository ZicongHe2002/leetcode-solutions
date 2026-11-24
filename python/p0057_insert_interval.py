class Solution:
    def insert(self, intervals, newInterval):
        result = []
        index = 0
        start, end = newInterval
        while index < len(intervals) and intervals[index][1] < start:
            result.append(intervals[index][:])
            index += 1
        while index < len(intervals) and intervals[index][0] <= end:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1
        result.append([start, end])
        while index < len(intervals):
            result.append(intervals[index][:])
            index += 1
        return result
