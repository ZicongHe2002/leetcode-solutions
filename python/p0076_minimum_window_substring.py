from collections import Counter


class Solution:
    def minWindow(self, s, t):
        if not t or len(t) > len(s):
            return ''
        needed = Counter(t)
        missing = len(t)
        left = best_start = 0
        best_length = len(s) + 1
        for right, character in enumerate(s):
            if needed[character] > 0:
                missing -= 1
            needed[character] -= 1
            while missing == 0:
                if right - left + 1 < best_length:
                    best_start, best_length = left, right - left + 1
                leaving = s[left]
                needed[leaving] += 1
                if needed[leaving] > 0:
                    missing += 1
                left += 1
        return '' if best_length > len(s) else s[best_start:best_start + best_length]
