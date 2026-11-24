class Solution:
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        best = [1] * len(s)
        for left in range(len(s) - 1, -1, -1):
            inner = 0
            for right in range(left + 1, len(s)):
                previous = best[right]
                if s[left] == s[right]:
                    best[right] = inner + 2
                else:
                    best[right] = max(best[right], best[right - 1])
                inner = previous
        return best[-1]
