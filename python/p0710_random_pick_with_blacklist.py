from random import randrange


class Solution:
    def __init__(self, n, blacklist):
        blocked = set(blacklist)
        self.limit = n - len(blocked)
        self.redirect = {}
        tail = self.limit
        for value in blacklist:
            if value < self.limit:
                while tail in blocked:
                    tail += 1
                self.redirect[value] = tail
                tail += 1

    def pick(self):
        rank = randrange(self.limit)
        return self.redirect.get(rank, rank)
