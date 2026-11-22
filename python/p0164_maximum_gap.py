class Solution:
    def maximumGap(self, nums):
        size = len(nums)
        if size < 2:
            return 0
        smallest, largest = min(nums), max(nums)
        if smallest == largest:
            return 0
        width = (largest - smallest + size - 2) // (size - 1)
        count = (largest - smallest) // width + 1
        minima, maxima = [None] * count, [None] * count
        for value in nums:
            index = (value - smallest) // width
            if minima[index] is None:
                minima[index] = maxima[index] = value
            else:
                minima[index] = min(minima[index], value)
                maxima[index] = max(maxima[index], value)
        previous, best = smallest, 0
        for low, high in zip(minima, maxima):
            if low is not None:
                best = max(best, low - previous)
                previous = high
        return best
