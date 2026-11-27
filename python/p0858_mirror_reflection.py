from math import gcd


class Solution:
    def mirrorReflection(self, p, q):
        divisor = gcd(p,q)
        horizontal = p // divisor
        vertical = q // divisor
        if horizontal % 2 == 0:
            return 2
        return 1 if vertical % 2 else 0
