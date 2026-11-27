class Solution:
    def makesquare(self, matchsticks):
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4:
            return False
        side = total // 4
        if max(matchsticks) > side:
            return False
        remainder = [-1] * (1 << len(matchsticks))
        remainder[0] = 0
        for mask, used in enumerate(remainder):
            if used < 0:
                continue
            for index, length in enumerate(matchsticks):
                bit = 1 << index
                if not mask & bit and used + length <= side:
                    remainder[mask | bit] = (used + length) % side
        return remainder[-1] == 0
