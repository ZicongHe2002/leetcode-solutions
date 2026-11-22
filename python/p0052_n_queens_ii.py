class Solution:
    def totalNQueens(self, n):
        full = (1 << n) - 1

        def search(columns, falling, rising):
            if columns == full:
                return 1
            available = full & ~(columns | falling | rising)
            total = 0
            while available:
                chosen = available & -available
                available -= chosen
                total += search(columns | chosen, ((falling | chosen) << 1) & full, (rising | chosen) >> 1)
            return total

        return search(0, 0, 0)
