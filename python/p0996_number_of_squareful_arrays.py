from collections import Counter
from functools import cache
from math import isqrt


class Solution:
    def numSquarefulPerms(self, nums):
        counts = Counter(nums)
        values = list(counts)
        neighbors = [[] for _ in values]
        for first,left in enumerate(values):
            for second,right in enumerate(values):
                total = left + right
                if isqrt(total)**2 == total:
                    neighbors[first].append(second)

        @cache
        def ways(last, remaining):
            if not any(remaining):
                return 1
            answer = 0
            for following in neighbors[last]:
                if remaining[following]:
                    after = list(remaining)
                    after[following] -= 1
                    answer += ways(following,tuple(after))
            return answer

        original = tuple(counts[value] for value in values)
        answer = 0
        for first in range(len(values)):
            remaining = list(original)
            remaining[first] -= 1
            answer += ways(first,tuple(remaining))
        return answer
