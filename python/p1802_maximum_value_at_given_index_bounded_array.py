class Solution:
    def maxValue(self, n, index, maxSum):
        def side_sum(length, peak):
            descending = min(length, peak - 1)
            return descending * (2 * peak - descending - 1) // 2 + length - descending

        def required(peak):
            return peak + side_sum(index, peak) + side_sum(n - index - 1, peak)

        low, high = 1, maxSum - n + 1
        while low < high:
            middle = (low + high + 1) // 2
            if required(middle) <= maxSum:
                low = middle
            else:
                high = middle - 1
        return low
