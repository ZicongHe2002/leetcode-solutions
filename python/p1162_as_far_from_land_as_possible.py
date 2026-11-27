from collections import deque


class Solution:
    def maxDistance(self, grid):
        size = len(grid)
        distance = [[-1] * size for _ in range(size)]
        pending = deque()
        for row in range(size):
            for column in range(size):
                if grid[row][column] == 1:
                    distance[row][column] = 0
                    pending.append((row, column))
        if not pending or len(pending) == size * size:
            return -1
        answer = 0
        while pending:
            row, column = pending.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < size and 0 <= nc < size and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[row][column] + 1
                    answer = max(answer, distance[nr][nc])
                    pending.append((nr, nc))
        return answer
