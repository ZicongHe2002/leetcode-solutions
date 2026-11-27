class Solution:
    def uniquePathsIII(self, grid):
        board = [row[:] for row in grid]
        rows,columns = len(board),len(board[0])
        total = 0
        for row in range(rows):
            for column in range(columns):
                if board[row][column] != -1:
                    total += 1
                if board[row][column] == 1:
                    start = row,column

        def walk(row, column, visited):
            if board[row][column] == 2:
                return int(visited == total)
            original = board[row][column]
            board[row][column] = -1
            paths = 0
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = row + dr,column + dc
                if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] != -1:
                    paths += walk(nr,nc,visited + 1)
            board[row][column] = original
            return paths

        return walk(start[0],start[1],1)
