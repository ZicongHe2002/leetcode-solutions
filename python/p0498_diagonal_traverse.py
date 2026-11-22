class Solution:
    def findDiagonalOrder(self, mat):
        rows, columns = len(mat), len(mat[0])
        output = []
        for diagonal in range(rows + columns - 1):
            if diagonal % 2 == 0:
                row = min(diagonal, rows - 1)
                column = diagonal - row
                while row >= 0 and column < columns:
                    output.append(mat[row][column])
                    row -= 1
                    column += 1
            else:
                column = min(diagonal, columns - 1)
                row = diagonal - column
                while column >= 0 and row < rows:
                    output.append(mat[row][column])
                    row += 1
                    column -= 1
        return output
