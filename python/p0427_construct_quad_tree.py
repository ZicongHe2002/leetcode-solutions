class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        size = len(grid)
        prefix = [[0] * (size + 1) for _ in range(size + 1)]
        for row, values in enumerate(grid):
            subtotal = 0
            for column, value in enumerate(values):
                subtotal += value
                prefix[row + 1][column + 1] = prefix[row][column + 1] + subtotal

        def build(row, column, width):
            end_row, end_column = row + width, column + width
            ones = prefix[end_row][end_column] - prefix[row][end_column] - prefix[end_row][column] + prefix[row][column]
            if ones == 0 or ones == width * width:
                return Node(bool(ones), True)
            half = width // 2
            return Node(False, False,
                        build(row, column, half), build(row, column + half, half),
                        build(row + half, column, half), build(row + half, column + half, half))

        return build(0, 0, size)
