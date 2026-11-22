class Solution:
    def transpose(self, matrix):
        return [[matrix[row][column] for row in range(len(matrix))]
                for column in range(len(matrix[0]))]
