class Solution:
    def minmaxGasDist(self, stations, k):
        scale = 10**7
        gaps = [right - left for left, right in zip(stations, stations[1:])]
        low, high = 1, max(gaps) * scale
        while low < high:
            middle = (low + high) // 2
            needed = sum((gap * scale - 1) // middle for gap in gaps)
            if needed <= k:
                high = middle
            else:
                low = middle + 1
        return low / scale
