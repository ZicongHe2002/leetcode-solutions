from bisect import bisect_left, bisect_right


class RangeModule:
    def __init__(self):
        self.boundaries = []

    def addRange(self, left, right):
        start = bisect_left(self.boundaries, left)
        end = bisect_right(self.boundaries, right)
        replacement = []
        if start % 2 == 0:
            replacement.append(left)
        if end % 2 == 0:
            replacement.append(right)
        self.boundaries[start:end] = replacement

    def queryRange(self, left, right):
        start = bisect_right(self.boundaries, left)
        end = bisect_left(self.boundaries, right)
        return start == end and start % 2 == 1

    def removeRange(self, left, right):
        start = bisect_left(self.boundaries, left)
        end = bisect_right(self.boundaries, right)
        replacement = []
        if start % 2 == 1:
            replacement.append(left)
        if end % 2 == 1:
            replacement.append(right)
        self.boundaries[start:end] = replacement
