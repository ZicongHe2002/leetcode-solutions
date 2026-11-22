from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        size = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        queue = deque([(0, 0, 1)])
        seen = {(0, 0)}
        while queue:
            row, column, length = queue.popleft()
            if row == column == size - 1:
                return length
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = row + dr, column + dc
                    if (dr or dc) and 0 <= nr < size and 0 <= nc < size and not grid[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc, length + 1))
        return -1
