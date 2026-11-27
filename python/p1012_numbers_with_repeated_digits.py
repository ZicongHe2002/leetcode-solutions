from functools import cache


class Solution:
    def numDupDigitsAtMostN(self, n):
        digits = tuple(map(int,str(n)))

        @cache
        def unique(position, mask, tight, started):
            if position == len(digits):
                return int(started)
            limit = digits[position] if tight else 9
            answer = 0
            for digit in range(limit + 1):
                following_tight = tight and digit == limit
                if not started and digit == 0:
                    answer += unique(position + 1,mask,following_tight,False)
                elif not mask & (1 << digit):
                    answer += unique(position + 1,mask | (1 << digit),following_tight,True)
            return answer

        return n - unique(0,0,True,False)
