from collections import defaultdict
from itertools import combinations


class Solution:
    def minAreaFreeRect(self, points):
        diagonals = defaultdict(list)
        for first in range(len(points)):
            x1,y1 = points[first]
            for second in range(first):
                x2,y2 = points[second]
                key = x1 + x2,y1 + y2,(x1 - x2)**2 + (y1 - y2)**2
                diagonals[key].append((first,second))
        best = float('inf')
        for group in diagonals.values():
            for first,second in combinations(group,2):
                x,y = points[first[0]]
                ax,ay = points[second[0]]
                bx,by = points[second[1]]
                area = abs((ax - x) * (by - y) - (ay - y) * (bx - x))
                if area:
                    best = min(best,area)
        return 0.0 if best == float('inf') else float(best)
