class Solution:
    def removeKdigits(self, num, k):
        kept = []
        remaining = k
        for digit in num:
            while remaining and kept and kept[-1] > digit:
                kept.pop()
                remaining -= 1
            kept.append(digit)
        if remaining:
            del kept[-remaining:]
        return ''.join(kept).lstrip('0') or '0'
