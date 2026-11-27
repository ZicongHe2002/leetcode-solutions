from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        counts = Counter(tuple(value ^ row[0] for value in row) for row in matrix)
        return max(counts.values())
