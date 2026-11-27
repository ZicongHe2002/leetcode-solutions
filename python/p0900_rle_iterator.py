class RLEIterator:
    def __init__(self, encoding):
        self.encoding = encoding[:]
        self.position = 0

    def next(self, n):
        while self.position < len(self.encoding):
            remaining = self.encoding[self.position]
            if n > remaining:
                n -= remaining
                self.position += 2
            else:
                self.encoding[self.position] -= n
                return self.encoding[self.position + 1]
        return -1
