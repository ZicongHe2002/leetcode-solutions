class Solution:
    def countNegatives(self, grid):
        row, column = len(grid) - 1, 0
        width = len(grid[0])
        result = 0
        while row >= 0 and column < width:
            if grid[row][column] < 0:
                result += width - column
                row -= 1
            else:
                column += 1
        return result
