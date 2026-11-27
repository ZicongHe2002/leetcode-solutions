from collections import deque


class Solution:
    def numEnclaves(self, grid):
        rows, columns = len(grid), len(grid[0])
        queue, reachable = deque(), set()

        def enter(row, column):
            cell = (row, column)
            if grid[row][column] == 1 and cell not in reachable:
                reachable.add(cell)
                queue.append(cell)

        for row in range(rows):
            enter(row, 0)
            enter(row, columns - 1)
        for column in range(columns):
            enter(0, column)
            enter(rows - 1, column)
        while queue:
            row, column = queue.popleft()
            for nr, nc in ((row - 1, column), (row + 1, column),
                           (row, column - 1), (row, column + 1)):
                if 0 <= nr < rows and 0 <= nc < columns:
                    enter(nr, nc)
        return sum(map(sum, grid)) - len(reachable)
