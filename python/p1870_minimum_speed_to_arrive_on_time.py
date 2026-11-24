from decimal import Decimal


class Solution:
    def minSpeedOnTime(self, dist, hour):
        hundredths = int(Decimal(str(hour)) * 100)

        def feasible(speed):
            whole_hours = sum((distance + speed - 1) // speed for distance in dist[:-1])
            return 100 * (whole_hours * speed + dist[-1]) <= hundredths * speed

        low, high = 1, 10**7
        if not feasible(high):
            return -1
        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1
        return low
