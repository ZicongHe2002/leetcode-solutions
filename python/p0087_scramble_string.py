from collections import Counter
from functools import lru_cache


class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False

        @lru_cache(None)
        def match(first, second, size):
            left = s1[first:first + size]
            right = s2[second:second + size]
            if left == right:
                return True
            if Counter(left) != Counter(right):
                return False
            for split in range(1, size):
                if (match(first, second, split)
                        and match(first + split, second + split, size - split)):
                    return True
                if (match(first, second + size - split, split)
                        and match(first + split, second, size - split)):
                    return True
            return False

        return match(0, 0, len(s1))
