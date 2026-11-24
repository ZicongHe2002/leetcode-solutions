class StockSpanner:
    def __init__(self):
        self._spans = []

    def next(self, price):
        span = 1
        while self._spans and self._spans[-1][0] <= price:
            span += self._spans.pop()[1]
        self._spans.append((price, span))
        return span
