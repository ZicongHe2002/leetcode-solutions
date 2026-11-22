class Solution:
    def subArrayRanges(self, nums):
        size = len(nums)

        def total_extrema(as_minimum):
            pending = []
            total = 0
            for right in range(size + 1):
                while pending and (
                    right == size or
                    (nums[pending[-1]] >= nums[right] if as_minimum else nums[pending[-1]] <= nums[right])
                ):
                    index = pending.pop()
                    left = pending[-1] if pending else -1
                    total += nums[index] * (index - left) * (right - index)
                if right < size:
                    pending.append(right)
            return total

        return total_extrema(False) - total_extrema(True)
