import heapq


class Solution:
    def minimumEffortPath(self, heights):
        rows, columns = len(heights), len(heights[0])
        best = [[1000000] * columns for _ in range(rows)]
        best[0][0] = 0
        pending = [(0, 0, 0)]
        while pending:
            effort, row, column = heapq.heappop(pending)
            if effort != best[row][column]:
                continue
            if row == rows - 1 and column == columns - 1:
                return effort
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < columns:
                    candidate = max(effort, abs(heights[nr][nc] - heights[row][column]))
                    if candidate < best[nr][nc]:
                        best[nr][nc] = candidate
                        heapq.heappush(pending, (candidate, nr, nc))
