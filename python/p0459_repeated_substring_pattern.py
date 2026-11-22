class Solution:
    def repeatedSubstringPattern(self, s):
        prefix = [0] * len(s)
        for index in range(1, len(s)):
            matched = prefix[index - 1]
            while matched and s[index] != s[matched]:
                matched = prefix[matched - 1]
            if s[index] == s[matched]:
                matched += 1
            prefix[index] = matched
        border = prefix[-1]
        return border > 0 and len(s) % (len(s) - border) == 0
