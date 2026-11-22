from functools import lru_cache


class Solution:
    def stoneGameII(self, piles):
        suffix = [0] * (len(piles) + 1)
        for index in range(len(piles) - 1, -1, -1):
            suffix[index] = suffix[index + 1] + piles[index]

        @lru_cache(None)
        def best(index, limit):
            if 2 * limit >= len(piles) - index:
                return suffix[index]
            return suffix[index] - min(best(index + taken, max(limit, taken))
                                       for taken in range(1, 2 * limit + 1))

        return best(0, 1)
