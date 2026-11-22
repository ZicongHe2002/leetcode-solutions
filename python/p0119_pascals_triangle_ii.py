class Solution:
    def getRow(self, rowIndex):
        row = [1]
        for level in range(1, rowIndex + 1):
            row.append(1)
            for column in range(level - 1, 0, -1):
                row[column] += row[column - 1]
        return row
