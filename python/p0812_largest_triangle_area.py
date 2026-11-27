from itertools import combinations


class Solution:
    def largestTriangleArea(self, points):
        twice_area = 0
        for first,second,third in combinations(points,3):
            cross = ((second[0] - first[0]) * (third[1] - first[1])
                     - (second[1] - first[1]) * (third[0] - first[0]))
            twice_area = max(twice_area,abs(cross))
        return twice_area / 2.0
