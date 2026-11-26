class Solution:
    def nearestPalindromic(self, n):
        length = len(n)
        value = int(n)
        width = (length + 1) // 2
        prefix = int(n[:width])
        candidates = {10 ** (length - 1) - 1, 10 ** length + 1}
        for half in (prefix - 1, prefix, prefix + 1):
            text = str(half)
            if len(text) != width:
                continue
            suffix = text[:-1] if length % 2 else text
            candidates.add(int(text + suffix[::-1]))
        candidates.discard(value)
        return str(min(candidates, key=lambda candidate: (abs(candidate - value), candidate)))
