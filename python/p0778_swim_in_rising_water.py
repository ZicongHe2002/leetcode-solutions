import heapq


class Solution:
    def swimInWater(self, grid):
        size = len(grid)
        best = [[size * size] * size for _ in range(size)]
        best[0][0] = grid[0][0]
        pending = [(grid[0][0], 0, 0)]
        while pending:
            level, row, column = heapq.heappop(pending)
            if level != best[row][column]:
                continue
            if row == size - 1 and column == size - 1:
                return level
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < size and 0 <= nc < size:
                    candidate = max(level, grid[nr][nc])
                    if candidate < best[nr][nc]:
                        best[nr][nc] = candidate
                        heapq.heappush(pending, (candidate, nr, nc))
