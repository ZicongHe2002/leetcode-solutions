class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        total = duration
        for index in range(1, len(timeSeries)):
            total += min(duration, timeSeries[index] - timeSeries[index - 1])
        return total
