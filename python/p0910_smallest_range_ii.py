class Solution:
    def smallestRangeII(self, nums, k):
        values = sorted(nums)
        best = values[-1] - values[0]
        for split in range(len(values) - 1):
            high = max(values[split] + k,values[-1] - k)
            low = min(values[0] + k,values[split + 1] - k)
            best = min(best,high - low)
        return best
