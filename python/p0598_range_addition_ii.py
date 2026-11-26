class Solution:
    def maxCount(self, m, n, ops):
        rows, columns = m, n
        for height, width in ops:
            rows = min(rows, height)
            columns = min(columns, width)
        return rows * columns
