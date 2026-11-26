class Solution:
    def minCut(self, s):
        if not s:
            return 0
        cuts = list(range(-1, len(s)))

        def extend(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cuts[right + 1] = min(cuts[right + 1], cuts[left] + 1)
                left -= 1
                right += 1

        for center in range(len(s)):
            extend(center, center)
            extend(center - 1, center)
        return cuts[-1]
