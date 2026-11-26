class Solution:
    def islandPerimeter(self, grid):
        perimeter = 0
        for row, values in enumerate(grid):
            for column, value in enumerate(values):
                if value == 1:
                    perimeter += 4
                    if row > 0 and grid[row - 1][column] == 1:
                        perimeter -= 2
                    if column > 0 and values[column - 1] == 1:
                        perimeter -= 2
        return perimeter
