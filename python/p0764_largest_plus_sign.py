class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        blocked = {tuple(cell) for cell in mines}
        order = [[0] * n for _ in range(n)]
        for row in range(n):
            run = 0
            for column in range(n):
                run = 0 if (row, column) in blocked else run + 1
                order[row][column] = run
            run = 0
            for column in range(n - 1, -1, -1):
                run = 0 if (row, column) in blocked else run + 1
                order[row][column] = min(order[row][column], run)
        best = 0
        for column in range(n):
            run = 0
            for row in range(n):
                run = 0 if (row, column) in blocked else run + 1
                order[row][column] = min(order[row][column], run)
            run = 0
            for row in range(n - 1, -1, -1):
                run = 0 if (row, column) in blocked else run + 1
                order[row][column] = min(order[row][column], run)
                best = max(best, order[row][column])
        return best
