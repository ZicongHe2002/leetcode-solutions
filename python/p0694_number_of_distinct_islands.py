class Solution:
    def numDistinctIslands(self, grid):
        rows, columns = len(grid), len(grid[0])
        visited, shapes = set(), set()
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0 or (row, column) in visited:
                    continue
                pending = [(row, column)]
                visited.add((row, column))
                shape = set()
                while pending:
                    r, c = pending.pop()
                    shape.add((r - row, c - column))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < columns
                                and grid[nr][nc] == 1 and (nr, nc) not in visited):
                            visited.add((nr, nc))
                            pending.append((nr, nc))
                shapes.add(frozenset(shape))
        return len(shapes)
