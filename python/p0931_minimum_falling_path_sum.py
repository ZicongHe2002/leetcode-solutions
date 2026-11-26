class Solution:
    def minFallingPathSum(self, matrix):
        size = len(matrix)
        previous = matrix[0][:]
        for row in range(1, size):
            current = []
            for column in range(size):
                best = previous[column]
                if column:
                    best = min(best, previous[column - 1])
                if column + 1 < size:
                    best = min(best, previous[column + 1])
                current.append(matrix[row][column] + best)
            previous = current
        return min(previous)
