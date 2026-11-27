class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        row,column = rStart,cStart
        result = [[row,column]]
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        direction = 0
        length = 1
        while len(result) < rows * cols:
            for _ in range(2):
                dr,dc = directions[direction % 4]
                for _ in range(length):
                    row += dr
                    column += dc
                    if 0 <= row < rows and 0 <= column < cols:
                        result.append([row,column])
                        if len(result) == rows * cols:
                            return result
                direction += 1
            length += 1
        return result
