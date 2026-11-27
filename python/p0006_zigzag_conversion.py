class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        row, direction = 0, 1
        for character in s:
            rows[row].append(character)
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        return ''.join(''.join(characters) for characters in rows)
