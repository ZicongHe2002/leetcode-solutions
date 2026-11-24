class Solution:
    def characterReplacement(self, s, k):
        counts = [0] * 26
        left = best = 0
        for right, character in enumerate(s):
            counts[ord(character) - ord('A')] += 1
            while right - left + 1 - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
