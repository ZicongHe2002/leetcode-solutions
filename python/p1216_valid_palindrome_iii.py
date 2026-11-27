class Solution:
    def isValidPalindrome(self, s, k):
        deletions = [0] * len(s)
        for left in range(len(s) - 2, -1, -1):
            diagonal = 0
            for right in range(left + 1, len(s)):
                previous = deletions[right]
                if s[left] == s[right]:
                    deletions[right] = diagonal
                else:
                    deletions[right] = 1 + min(deletions[right], deletions[right - 1])
                diagonal = previous
        return deletions[-1] <= k
