from collections import deque


class Solution:
    def hasValidPath(self, grid):
        ports = {
            1: ((0, -1), (0, 1)),
            2: ((-1, 0), (1, 0)),
            3: ((0, -1), (1, 0)),
            4: ((0, 1), (1, 0)),
            5: ((0, -1), (-1, 0)),
            6: ((0, 1), (-1, 0)),
        }
        rows, columns = len(grid), len(grid[0])
        queue, seen = deque([(0, 0)]), {(0, 0)}
        while queue:
            row, column = queue.popleft()
            if row == rows - 1 and column == columns - 1:
                return True
            for dr, dc in ports[grid[row][column]]:
                nr, nc = row + dr, column + dc
                if not (0 <= nr < rows and 0 <= nc < columns):
                    continue
                if (-dr, -dc) not in ports[grid[nr][nc]] or (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                queue.append((nr, nc))
        return False
