class Solution:
    def countBinarySubstrings(self, s):
        previous, current, total = 0, 1, 0
        for index in range(1, len(s)):
            if s[index] == s[index - 1]:
                current += 1
            else:
                total += min(previous, current)
                previous, current = current, 1
        return total + min(previous, current)
