from math import isqrt


class Solution:
    def numSquares(self, n):
        squares = [value * value for value in range(1, isqrt(n) + 1)]
        counts = [0] + [n + 1] * n
        for value in range(1, n + 1):
            for square in squares:
                if square > value:
                    break
                counts[value] = min(counts[value], counts[value - square] + 1)
        return counts[n]
