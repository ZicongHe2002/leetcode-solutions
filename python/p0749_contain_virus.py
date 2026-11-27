class Solution:
    def containVirus(self, isInfected):
        board = [row[:] for row in isInfected]
        rows, columns, total = len(board), len(board[0]), 0
        while True:
            seen, regions = set(), []
            for row in range(rows):
                for column in range(columns):
                    if board[row][column] != 1 or (row, column) in seen:
                        continue
                    stack, cells, frontier, walls = [(row, column)], [], set(), 0
                    seen.add((row, column))
                    while stack:
                        current_row, current_column = stack.pop()
                        cells.append((current_row, current_column))
                        for next_row, next_column in ((current_row - 1, current_column),
                                                      (current_row + 1, current_column),
                                                      (current_row, current_column - 1),
                                                      (current_row, current_column + 1)):
                            if not (0 <= next_row < rows and 0 <= next_column < columns):
                                continue
                            if board[next_row][next_column] == 0:
                                frontier.add((next_row, next_column))
                                walls += 1
                            elif board[next_row][next_column] == 1 and (next_row, next_column) not in seen:
                                seen.add((next_row, next_column))
                                stack.append((next_row, next_column))
                    regions.append((cells, frontier, walls))
            if not regions:
                return total
            chosen = max(range(len(regions)), key=lambda index: len(regions[index][1]))
            if not regions[chosen][1]:
                return total
            total += regions[chosen][2]
            for row, column in regions[chosen][0]:
                board[row][column] = -1
            for index, (_, frontier, _) in enumerate(regions):
                if index != chosen:
                    for row, column in frontier:
                        board[row][column] = 1
