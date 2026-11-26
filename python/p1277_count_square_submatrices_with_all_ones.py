class Solution:
    def countSquares(self, matrix):
        squares = [0] * (len(matrix[0]) + 1)
        total = 0
        for row in matrix:
            diagonal = 0
            for column, value in enumerate(row, 1):
                above = squares[column]
                squares[column] = 1 + min(above, squares[column - 1], diagonal) if value else 0
                total += squares[column]
                diagonal = above
        return total
