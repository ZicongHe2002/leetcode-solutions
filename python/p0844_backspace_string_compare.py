class Solution:
    def backspaceCompare(self, s, t):
        def previous_visible(text, index):
            skipped = 0
            while index >= 0:
                if text[index] == '#':
                    skipped += 1
                elif skipped:
                    skipped -= 1
                else:
                    return index
                index -= 1
            return -1

        left, right = len(s) - 1, len(t) - 1
        while True:
            left = previous_visible(s, left)
            right = previous_visible(t, right)
            if left < 0 or right < 0:
                return left == right
            if s[left] != t[right]:
                return False
            left -= 1
            right -= 1
