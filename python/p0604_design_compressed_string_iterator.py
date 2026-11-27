class StringIterator:
    def __init__(self, compressedString):
        self.compressed = compressedString
        self.index = 0
        self.remaining = 0
        self.current = ' '

    def next(self):
        if not self.hasNext():
            return ' '
        if self.remaining == 0:
            self.current = self.compressed[self.index]
            self.index += 1
            count = 0
            while self.index < len(self.compressed) and self.compressed[self.index].isdigit():
                count = count * 10 + int(self.compressed[self.index])
                self.index += 1
            self.remaining = count
        self.remaining -= 1
        return self.current

    def hasNext(self):
        return self.remaining > 0 or self.index < len(self.compressed)
