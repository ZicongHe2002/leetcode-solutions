class Solution:
    def numberOfLines(self, widths, s):
        lines, used = 1, 0
        for char in s:
            width = widths[ord(char) - ord('a')]
            if used + width > 100:
                lines += 1
                used = 0
            used += width
        return [lines,used]
