class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        columns = len(grid[0])
        costs = [grid[0][0]]
        for column in range(1, columns):
            costs.append(costs[-1] + grid[0][column])
        for row_index in range(1, len(grid)):
            row = grid[row_index]
            costs[0] += row[0]
            for column in range(1, columns):
                costs[column] = min(costs[column], costs[column - 1]) + row[column]
        return costs[-1]
