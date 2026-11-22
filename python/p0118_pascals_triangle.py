class Solution:
    def generate(self, numRows):
        triangle = []
        for level in range(numRows):
            row = [1] * (level + 1)
            for column in range(1, level):
                row[column] = triangle[-1][column - 1] + triangle[-1][column]
            triangle.append(row)
        return triangle
