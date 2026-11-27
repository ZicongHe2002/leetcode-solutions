from collections import Counter
from math import comb


class Solution:
    def threeSumMulti(self, arr, target):
        counts = Counter(arr)
        values = sorted(counts)
        answer = 0
        for first_index,first in enumerate(values):
            for second in values[first_index:]:
                third = target - first - second
                if third < second:
                    break
                if third not in counts:
                    continue
                if first == third:
                    answer += comb(counts[first],3)
                elif first == second:
                    answer += comb(counts[first],2) * counts[third]
                elif second == third:
                    answer += counts[first] * comb(counts[second],2)
                else:
                    answer += counts[first] * counts[second] * counts[third]
        return answer % (10**9 + 7)
