class Solution:
    def findKthNumber(self, m, n, k):
        if m > n:
            m, n = n, m
        lower, upper = 1, m * n
        while lower < upper:
            middle = (lower + upper) // 2
            count = 0
            for row in range(1, min(m, middle) + 1):
                count += min(n, middle // row)
                if count >= k:
                    break
            if count >= k:
                upper = middle
            else:
                lower = middle + 1
        return lower
