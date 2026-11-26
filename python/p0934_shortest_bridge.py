from collections import deque


class Solution:
    def shortestBridge(self, grid):
        size = len(grid)
        first = next((row, column) for row in range(size) for column in range(size) if grid[row][column])
        seen, pending, frontier = {first}, [first], deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while pending:
            row, column = pending.pop()
            frontier.append((row, column, 0))
            for dr, dc in directions:
                nr, nc = row + dr, column + dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    pending.append((nr, nc))
        while frontier:
            row, column, water = frontier.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, column + dc
                if not (0 <= nr < size and 0 <= nc < size) or (nr, nc) in seen:
                    continue
                if grid[nr][nc]:
                    return water
                seen.add((nr, nc))
                frontier.append((nr, nc, water + 1))
        return -1
