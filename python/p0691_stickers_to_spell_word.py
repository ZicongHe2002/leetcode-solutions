from collections import Counter
from functools import lru_cache


class Solution:
    def minStickers(self, stickers, target):
        needed = Counter(target)
        letters = tuple(sorted(needed))
        supplies = []
        for word in stickers:
            counts = Counter(word)
            supplies.append(tuple(counts[letter] for letter in letters))

        @lru_cache(None)
        def minimum(remaining):
            if not any(remaining):
                return 0
            first = next(i for i, count in enumerate(remaining) if count)
            best = len(target) + 1
            for available in supplies:
                if available[first] == 0:
                    continue
                following = tuple(max(0, count - have) for count, have in zip(remaining, available))
                used = minimum(following)
                if used >= 0:
                    best = min(best, used + 1)
            return -1 if best > len(target) else best

        return minimum(tuple(needed[letter] for letter in letters))
