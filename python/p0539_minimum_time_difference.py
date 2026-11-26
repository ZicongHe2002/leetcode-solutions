class Solution:
    def findMinDifference(self, timePoints):
        present = [False] * 1440
        for text in timePoints:
            minute = int(text[:2]) * 60 + int(text[3:])
            if present[minute]:
                return 0
            present[minute] = True
        first = previous = None
        best = 1440
        for minute, exists in enumerate(present):
            if not exists:
                continue
            if previous is None:
                first = minute
            else:
                best = min(best, minute - previous)
            previous = minute
        return min(best, 1440 - previous + first)
