class Solution:
    def findNumberOfLIS(self, nums):
        lengths = [1] * len(nums)
        counts = [1] * len(nums)
        for right in range(len(nums)):
            for left in range(right):
                if nums[left] >= nums[right]:
                    continue
                extended = lengths[left] + 1
                if extended > lengths[right]:
                    lengths[right] = extended
                    counts[right] = counts[left]
                elif extended == lengths[right]:
                    counts[right] += counts[left]
        longest = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == longest)
