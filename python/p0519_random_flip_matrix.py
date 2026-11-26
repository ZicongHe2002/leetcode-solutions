from random import randrange


class Solution:
    def __init__(self, m, n):
        self.columns = n
        self.total = m * n
        self.remaining = self.total
        self.remap = {}

    def flip(self):
        index = randrange(self.remaining)
        self.remaining -= 1
        chosen = self.remap.get(index, index)
        self.remap[index] = self.remap.get(self.remaining, self.remaining)
        self.remap.pop(self.remaining, None)
        return [chosen // self.columns, chosen % self.columns]

    def reset(self):
        self.remaining = self.total
        self.remap.clear()
