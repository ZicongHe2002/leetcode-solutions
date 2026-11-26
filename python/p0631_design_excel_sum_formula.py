from collections import Counter


class Excel:
    def __init__(self, height, width):
        self._values = {}
        self._formulas = {}

    def set(self, row, column, val):
        cell = (row, column)
        self._formulas.pop(cell, None)
        self._values[cell] = val

    def get(self, row, column):
        memo = {}

        def evaluate(cell):
            if cell not in memo:
                if cell in self._formulas:
                    memo[cell] = sum(count * evaluate(source)
                                     for source, count in self._formulas[cell].items())
                else:
                    memo[cell] = self._values.get(cell, 0)
            return memo[cell]

        return evaluate((row, column))

    def sum(self, row, column, numbers):
        references = Counter()
        for term in numbers:
            endpoints = term.split(':')
            start, end = endpoints[0], endpoints[-1]
            references.update((r, chr(c))
                              for r in range(int(start[1:]), int(end[1:]) + 1)
                              for c in range(ord(start[0]), ord(end[0]) + 1))
        cell = (row, column)
        self._formulas[cell] = references
        self._values.pop(cell, None)
        return self.get(row, column)
