class Solution:
    def solveNQueens(self, n):
        result, placement = [], []
        columns, falling, rising = set(), set(), set()

        def search(row):
            if row == n:
                result.append(['.' * column + 'Q' + '.' * (n - column - 1) for column in placement])
                return
            for column in range(n):
                if column in columns or row - column in falling or row + column in rising:
                    continue
                columns.add(column)
                falling.add(row - column)
                rising.add(row + column)
                placement.append(column)
                search(row + 1)
                placement.pop()
                rising.remove(row + column)
                falling.remove(row - column)
                columns.remove(column)

        search(0)
        return result
