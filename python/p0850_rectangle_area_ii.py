from collections import Counter
from itertools import groupby


class Solution:
    def rectangleArea(self, rectangles):
        events = []
        for left,bottom,right,top in rectangles:
            events.append((left,1,bottom,top))
            events.append((right,-1,bottom,top))
        events.sort()
        active = Counter()
        previous = events[0][0]
        covered = area = 0
        modulus = 10**9 + 7
        for x,group in groupby(events,key=lambda event:event[0]):
            area = (area + (x - previous) * covered) % modulus
            for _,change,bottom,top in group:
                interval = bottom,top
                active[interval] += change
                if active[interval] == 0:
                    del active[interval]
            covered = 0
            end = None
            for bottom,top in sorted(active):
                if end is None or bottom > end:
                    covered += top - bottom
                    end = top
                elif top > end:
                    covered += top - end
                    end = top
            previous = x
        return area
