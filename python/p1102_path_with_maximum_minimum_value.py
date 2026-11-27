from heapq import heappop, heappush


class Solution:
    def maximumMinimumPath(self, grid):
        rows, columns = len(grid), len(grid[0])
        pending = [(-grid[0][0], 0, 0)]
        visited = set()
        while pending:
            negative_score, row, column = heappop(pending)
            if (row, column) in visited:
                continue
            visited.add((row, column))
            score = -negative_score
            if row == rows - 1 and column == columns - 1:
                return score
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited:
                    heappush(pending, (-min(score, grid[nr][nc]), nr, nc))
