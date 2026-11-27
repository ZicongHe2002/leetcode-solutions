class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        row = [float(poured)]
        for _ in range(query_row):
            following = [0.0] * (len(row) + 1)
            for column,amount in enumerate(row):
                overflow = max(0.0,(amount - 1.0) / 2.0)
                following[column] += overflow
                following[column + 1] += overflow
            row = following
        return min(1.0,row[query_glass])
