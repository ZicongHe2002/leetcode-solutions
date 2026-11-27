class Solution:
    def largest1BorderedSquare(self, grid):
        rows, columns = len(grid), len(grid[0])
        left = [[0] * columns for _ in range(rows)]
        up = [[0] * columns for _ in range(rows)]
        best = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:
                    continue
                left[row][column] = 1 + (left[row][column - 1] if column else 0)
                up[row][column] = 1 + (up[row - 1][column] if row else 0)
                side = min(left[row][column], up[row][column])
                while side > best:
                    if left[row - side + 1][column] >= side and up[row][column - side + 1] >= side:
                        best = side
                        break
                    side -= 1
        return best * best
