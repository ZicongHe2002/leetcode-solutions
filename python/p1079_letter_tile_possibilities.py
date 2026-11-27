from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles):
        counts = Counter(tiles)

        def extend():
            total = 0
            for letter in counts:
                if counts[letter]:
                    counts[letter] -= 1
                    total += 1 + extend()
                    counts[letter] += 1
            return total

        return extend()
