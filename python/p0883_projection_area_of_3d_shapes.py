class Solution:
    def projectionArea(self, grid):
        top = sum(value > 0 for row in grid for value in row)
        front = sum(max(row) for row in grid)
        side = sum(max(column) for column in zip(*grid))
        return top + front + side
