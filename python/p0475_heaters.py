from bisect import bisect_left


class Solution:
    def findRadius(self, houses, heaters):
        ordered = sorted(heaters)
        radius = 0
        for house in houses:
            position = bisect_left(ordered, house)
            distance = abs(house - ordered[min(position, len(ordered) - 1)])
            if position:
                distance = min(distance, house - ordered[position - 1])
            radius = max(radius, distance)
        return radius
