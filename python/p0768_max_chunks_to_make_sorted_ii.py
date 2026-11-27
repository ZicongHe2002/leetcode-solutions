class Solution:
    def maxChunksToSorted(self, arr):
        maxima = []
        for value in arr:
            if not maxima or value >= maxima[-1]:
                maxima.append(value)
            else:
                maximum = maxima.pop()
                while maxima and maxima[-1] > value:
                    maxima.pop()
                maxima.append(maximum)
        return len(maxima)
