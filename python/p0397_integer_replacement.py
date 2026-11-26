from functools import lru_cache


class Solution:
    def integerReplacement(self, n):
        @lru_cache(None)
        def steps(value):
            if value == 1:
                return 0
            if value % 2 == 0:
                return 1 + steps(value // 2)
            return 2 + min(steps(value // 2), steps(value // 2 + 1))

        return steps(n)
