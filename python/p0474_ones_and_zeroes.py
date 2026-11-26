class Solution:
    def findMaxForm(self, strs, m, n):
        best = [[0] * (n + 1) for _ in range(m + 1)]
        for text in strs:
            zeros = text.count('0')
            ones = len(text) - zeros
            for zero_budget in range(m, zeros - 1, -1):
                for one_budget in range(n, ones - 1, -1):
                    best[zero_budget][one_budget] = max(
                        best[zero_budget][one_budget],
                        best[zero_budget - zeros][one_budget - ones] + 1)
        return best[m][n]
