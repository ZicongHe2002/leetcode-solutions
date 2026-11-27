class Solution:
    def isToeplitzMatrix(self, matrix):
        return all(matrix[row][column] == matrix[row - 1][column - 1]
                   for row in range(1, len(matrix)) for column in range(1, len(matrix[0])))
