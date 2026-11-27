class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        row_maximum = [max(row) for row in grid]
        column_maximum = [max(column) for column in zip(*grid)]
        return sum(min(row_maximum[row],column_maximum[column]) - height
                   for row,values in enumerate(grid) for column,height in enumerate(values))
