class Solution:
    def smallestDistancePair(self, nums, k):
        ordered = sorted(nums)
        low, high = 0, ordered[-1] - ordered[0]
        while low < high:
            distance = (low + high) // 2
            left = pairs = 0
            for right, value in enumerate(ordered):
                while value - ordered[left] > distance:
                    left += 1
                pairs += right - left
            if pairs >= k:
                high = distance
            else:
                low = distance + 1
        return low
