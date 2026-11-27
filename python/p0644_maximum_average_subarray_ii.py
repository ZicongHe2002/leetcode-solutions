class Solution:
    def findMaxAverage(self, nums, k):
        def feasible(target):
            total = delayed_total = 0
            minimum_prefix = 0.0
            for end, value in enumerate(nums, 1):
                total += value
                if end >= k:
                    if end > k:
                        delayed_total += nums[end - k - 1]
                        minimum_prefix = min(minimum_prefix,
                                             delayed_total - (end - k) * target)
                    if total - end * target >= minimum_prefix:
                        return True
            return False

        lower, upper = float(min(nums)), float(max(nums))
        for _ in range(60):
            middle = (lower + upper) / 2
            if feasible(middle):
                lower = middle
            else:
                upper = middle
        return lower
