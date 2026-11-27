class Solution:
    def cherryPickup(self, grid):
        size = len(grid)
        current = [[-1] * size for _ in range(size)]
        current[0][0] = grid[0][0]
        for step in range(1, 2 * size - 1):
            following = [[-1] * size for _ in range(size)]
            low, high = max(0, step - size + 1), min(size - 1, step)
            for first in range(low, high + 1):
                first_column = step - first
                if grid[first][first_column] == -1:
                    continue
                for second in range(low, high + 1):
                    second_column = step - second
                    if grid[second][second_column] == -1:
                        continue
                    best = current[first][second]
                    if first:
                        best = max(best, current[first - 1][second])
                    if second:
                        best = max(best, current[first][second - 1])
                    if first and second:
                        best = max(best, current[first - 1][second - 1])
                    if best < 0:
                        continue
                    gain = grid[first][first_column]
                    if first != second:
                        gain += grid[second][second_column]
                    following[first][second] = best + gain
            current = following
        return max(0, current[-1][-1])
