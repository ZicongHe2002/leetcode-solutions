from itertools import combinations


class Solution:
    def countCornerRectangles(self, grid):
        previous, total = {}, 0
        for row in grid:
            columns = [column for column, value in enumerate(row) if value == 1]
            for pair in combinations(columns, 2):
                count = previous.get(pair, 0)
                total += count
                previous[pair] = count + 1
        return total
