class Solution:
    def isSubsequence(self, s, t):
        matched = 0
        for character in t:
            if matched < len(s) and character == s[matched]:
                matched += 1
        return matched == len(s)
