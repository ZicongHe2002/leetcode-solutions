class Solution:
    def findMinArrowShots(self, points):
        arrows = 0
        position = None
        for start, end in sorted(points, key=lambda point: point[1]):
            if position is None or start > position:
                position = end
                arrows += 1
        return arrows
