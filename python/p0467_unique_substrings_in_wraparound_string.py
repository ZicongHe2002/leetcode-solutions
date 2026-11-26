class Solution:
    def findSubstringInWraproundString(self, s):
        longest = [0] * 26
        run = 0
        previous = -1
        for char in s:
            current = ord(char) - ord('a')
            run = run + 1 if previous >= 0 and (current - previous) % 26 == 1 else 1
            longest[current] = max(longest[current], run)
            previous = current
        return sum(longest)
