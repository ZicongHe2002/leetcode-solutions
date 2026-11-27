from collections import Counter


class Solution:
    def gridIllumination(self, n, lamps, queries):
        active = {tuple(point) for point in lamps}
        rows = Counter()
        columns = Counter()
        diagonal = Counter()
        antidiagonal = Counter()
        for row,column in active:
            rows[row] += 1
            columns[column] += 1
            diagonal[row - column] += 1
            antidiagonal[row + column] += 1
        answer = []
        for row,column in queries:
            answer.append(int(rows[row] > 0 or columns[column] > 0
                              or diagonal[row - column] > 0 or antidiagonal[row + column] > 0))
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    point = row + dr,column + dc
                    if point in active:
                        active.remove(point)
                        nr,nc = point
                        rows[nr] -= 1
                        columns[nc] -= 1
                        diagonal[nr - nc] -= 1
                        antidiagonal[nr + nc] -= 1
        return answer
