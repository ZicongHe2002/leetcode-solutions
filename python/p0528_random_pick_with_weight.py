from bisect import bisect_right
from random import randrange


class Solution:
    def __init__(self, w):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)

    def pickIndex(self):
        slot = randrange(self.prefix[-1])
        return bisect_right(self.prefix, slot)
