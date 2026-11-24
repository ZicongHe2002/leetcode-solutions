from collections import deque


class Solution:
    def orangesRotting(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        pending = deque()
        fresh = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    pending.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1
        minutes = 0
        while pending and fresh:
            for _ in range(len(pending)):
                row, column = pending.popleft()
                for nr, nc in ((row - 1, column), (row + 1, column),
                               (row, column - 1), (row, column + 1)):
                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        pending.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
