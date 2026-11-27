from bisect import bisect_right
from collections import defaultdict


class Solution:
    def shortestWay(self, source, target):
        positions = defaultdict(list)
        for index,char in enumerate(source):
            positions[char].append(index)
        if not target:
            return 0
        rounds = 1
        previous = -1
        for char in target:
            if char not in positions:
                return -1
            occurrences = positions[char]
            following = bisect_right(occurrences,previous)
            if following == len(occurrences):
                rounds += 1
                previous = occurrences[0]
            else:
                previous = occurrences[following]
        return rounds
