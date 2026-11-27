from collections import defaultdict
from itertools import combinations


class Solution:
    def minAreaRect(self, points):
        columns = defaultdict(list)
        for x,y in points:
            columns[x].append(y)
        previous = {}
        best = float('inf')
        for x in sorted(columns):
            for bottom,top in combinations(sorted(columns[x]),2):
                side = bottom,top
                if side in previous:
                    best = min(best,(x - previous[side]) * (top - bottom))
                previous[side] = x
        return 0 if best == float('inf') else best
