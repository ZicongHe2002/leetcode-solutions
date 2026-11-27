from math import isqrt


class Solution:
    def constructRectangle(self, area):
        width = isqrt(area)
        while area % width:
            width -= 1
        return [area // width, width]
