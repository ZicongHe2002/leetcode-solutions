class NumMatrix:
    def __init__(self, matrix):
        rows, columns = len(matrix), len(matrix[0])
        self._prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows):
            running = 0
            for column in range(columns):
                running += matrix[row][column]
                self._prefix[row + 1][column + 1] = self._prefix[row][column + 1] + running

    def sumRegion(self, row1, col1, row2, col2):
        prefix = self._prefix
        return (prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1]
                - prefix[row2 + 1][col1] + prefix[row1][col1])
