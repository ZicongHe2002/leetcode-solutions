class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        visited = set()
        largest = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] != 1 or (row, column) in visited:
                    continue
                visited.add((row, column))
                pending = [(row, column)]
                area = 0
                while pending:
                    current_row, current_column = pending.pop()
                    area += 1
                    for nr, nc in ((current_row - 1, current_column),
                                   (current_row + 1, current_column),
                                   (current_row, current_column - 1),
                                   (current_row, current_column + 1)):
                        if (0 <= nr < rows and 0 <= nc < columns
                                and grid[nr][nc] == 1 and (nr, nc) not in visited):
                            visited.add((nr, nc))
                            pending.append((nr, nc))
                largest = max(largest, area)
        return largest
