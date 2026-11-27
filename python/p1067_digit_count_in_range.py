from functools import cache


class Solution:
    def digitsCount(self, d, low, high):
        def count_up_to(bound):
            if bound <= 0:
                return 0
            digits = tuple(map(int,str(bound)))

            @cache
            def count(position, tight, started):
                if position == len(digits):
                    return (1,0) if started else (0,0)
                limit = digits[position] if tight else 9
                total_ways = total_digits = 0
                for digit in range(limit + 1):
                    following_started = started or digit != 0
                    ways,occurrences = count(position + 1,tight and digit == limit,following_started)
                    total_ways += ways
                    total_digits += occurrences
                    if following_started and digit == d:
                        total_digits += ways
                return total_ways,total_digits

            return count(0,True,False)[1]

        return count_up_to(high) - count_up_to(low - 1)
