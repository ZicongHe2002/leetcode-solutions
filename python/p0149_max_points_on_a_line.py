from math import gcd


class Solution:
    def maxPoints(self, points):
        best = 0
        for first in range(len(points)):
            directions = {}
            best = max(best, 1)
            for second in range(first + 1, len(points)):
                dx = points[second][0] - points[first][0]
                dy = points[second][1] - points[first][1]
                divisor = gcd(dx, dy)
                dx //= divisor
                dy //= divisor
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                direction = (dx, dy)
                directions[direction] = directions.get(direction, 0) + 1
                best = max(best, directions[direction] + 1)
        return best
