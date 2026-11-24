class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        lengths = [0] * (len(matrix[0]) + 1)
        largest = 0
        for row in matrix:
            diagonal = 0
            for column, value in enumerate(row, 1):
                above = lengths[column]
                if value == '1':
                    lengths[column] = 1 + min(above, lengths[column - 1], diagonal)
                    largest = max(largest, lengths[column])
                else:
                    lengths[column] = 0
                diagonal = above
        return largest * largest
