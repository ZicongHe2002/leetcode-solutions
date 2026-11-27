class Solution:
    def intersectionSizeTwo(self, intervals):
        first = second = -1
        count = 0
        for start, end in sorted(intervals, key=lambda item: (item[1], -item[0])):
            if start > second:
                first, second = end - 1, end
                count += 2
            elif start > first:
                first, second = second, end
                count += 1
        return count
