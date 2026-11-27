# LeetCode supplies the Interval(start, end) class.


class Solution:
    def employeeFreeTime(self, schedule):
        busy = sorted((interval.start, interval.end) for employee in schedule for interval in employee)
        end = busy[0][1]
        result = []
        for start, following_end in busy[1:]:
            if start > end:
                result.append(Interval(end, start))
            end = max(end, following_end)
        return result
