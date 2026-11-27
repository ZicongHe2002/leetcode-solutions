class Solution:
    def maxA(self, n):
        best = [0] * (n + 1)
        for presses in range(1, n + 1):
            best[presses] = best[presses - 1] + 1
            for copied_at in range(1, presses - 2):
                best[presses] = max(best[presses], best[copied_at] * (presses - copied_at - 1))
        return best[n]
