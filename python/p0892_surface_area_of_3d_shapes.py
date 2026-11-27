class Solution:
    def surfaceArea(self, grid):
        area = 0
        for row,values in enumerate(grid):
            for column,height in enumerate(values):
                if height:
                    area += 4 * height + 2
                    if row:
                        area -= 2 * min(height,grid[row - 1][column])
                    if column:
                        area -= 2 * min(height,grid[row][column - 1])
        return area
