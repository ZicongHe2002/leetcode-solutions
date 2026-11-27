class Solution:
    def solveSudoku(self, board):
        full = (1 << 9) - 1
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9
        empty = []
        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == '.':
                    empty.append((row, column))
                else:
                    bit = 1 << (ord(value) - ord('1'))
                    rows[row] |= bit
                    columns[column] |= bit
                    boxes[row // 3 * 3 + column // 3] |= bit

        def candidates(row, column):
            return full & ~(rows[row] | columns[column]
                            | boxes[row // 3 * 3 + column // 3])

        def fill(index):
            if index == len(empty):
                return True
            best = min(range(index, len(empty)),
                       key=lambda position: candidates(*empty[position]).bit_count())
            empty[index], empty[best] = empty[best], empty[index]
            row, column = empty[index]
            box = row // 3 * 3 + column // 3
            available = candidates(row, column)
            while available:
                bit = available & -available
                available ^= bit
                board[row][column] = str(bit.bit_length())
                rows[row] |= bit
                columns[column] |= bit
                boxes[box] |= bit
                if fill(index + 1):
                    return True
                rows[row] ^= bit
                columns[column] ^= bit
                boxes[box] ^= bit
                board[row][column] = '.'
            empty[index], empty[best] = empty[best], empty[index]
            return False

        fill(0)
