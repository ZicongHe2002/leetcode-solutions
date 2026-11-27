from collections import Counter
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck):
        common = 0
        for count in Counter(deck).values():
            common = gcd(common,count)
            if common == 1:
                return False
        return common >= 2
