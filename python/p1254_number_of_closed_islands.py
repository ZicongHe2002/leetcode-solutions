from collections import deque


class Solution:
    def closedIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        seen = set()
        result = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] or (row, column) in seen:
                    continue
                queue = deque([(row, column)])
                seen.add((row, column))
                closed = True
                while queue:
                    cr, cc = queue.popleft()
                    if cr in (0, rows - 1) or cc in (0, columns - 1):
                        closed = False
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < columns and not grid[nr][nc] and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
                result += closed
        return result
