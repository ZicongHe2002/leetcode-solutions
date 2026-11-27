class Solution:
    def minSwaps(self, data):
        width = sum(data)
        if width <= 1:
            return 0
        ones = sum(data[:width])
        best = ones
        for right in range(width, len(data)):
            ones += data[right] - data[right - width]
            best = max(best, ones)
        return width - best
