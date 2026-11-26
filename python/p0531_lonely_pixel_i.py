class Solution:
    def findLonelyPixel(self, picture):
        rows, columns = len(picture), len(picture[0])
        row_black = [0] * rows
        column_black = [0] * columns
        for row in range(rows):
            for column in range(columns):
                if picture[row][column] == 'B':
                    row_black[row] += 1
                    column_black[column] += 1
        return sum(picture[row][column] == 'B' and
                   row_black[row] == 1 and column_black[column] == 1
                   for row in range(rows) for column in range(columns))
