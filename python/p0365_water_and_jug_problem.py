from math import gcd


class Solution:
    def canMeasureWater(self, x, y, target):
        if target == 0:
            return True
        if target > x + y:
            return False
        return target % gcd(x, y) == 0
