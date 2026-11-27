from collections import deque


class Solution:
    def minimumMoves(self, grid):
        size = len(grid)
        pending = deque([(0, 0, 0, 0)])
        visited = {(0, 0, 0)}
        while pending:
            row, column, vertical, moves = pending.popleft()
            if (row, column, vertical) == (size - 1, size - 2, 0):
                return moves
            candidates = []
            if vertical == 0:
                if column + 2 < size and grid[row][column + 2] == 0:
                    candidates.append((row, column + 1, 0))
                if row + 1 < size and grid[row + 1][column] == grid[row + 1][column + 1] == 0:
                    candidates.extend(((row + 1, column, 0), (row, column, 1)))
            else:
                if row + 2 < size and grid[row + 2][column] == 0:
                    candidates.append((row + 1, column, 1))
                if column + 1 < size and grid[row][column + 1] == grid[row + 1][column + 1] == 0:
                    candidates.extend(((row, column + 1, 1), (row, column, 0)))
            for state in candidates:
                if state not in visited:
                    visited.add(state)
                    pending.append((*state, moves + 1))
        return -1
