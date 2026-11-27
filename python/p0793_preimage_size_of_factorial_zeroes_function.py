class Solution:
    def preimageSizeFZF(self, k):
        def first_at_least(threshold):
            low, high = 0, 5 * threshold
            while low < high:
                middle = (low + high) // 2
                quotient, zeroes = middle, 0
                while quotient:
                    quotient //= 5
                    zeroes += quotient
                if zeroes >= threshold:
                    high = middle
                else:
                    low = middle + 1
            return low

        return first_at_least(k + 1) - first_at_least(k)
