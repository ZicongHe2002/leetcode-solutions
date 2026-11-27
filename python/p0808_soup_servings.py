class Solution:
    def soupServings(self, n):
        units = (n + 24) // 25
        if units >= 500:
            return 1.0
        probability = [[0.0] * (units + 1) for _ in range(units + 1)]
        probability[0] = [0.5] + [1.0] * units
        for first in range(1,units + 1):
            for second in range(1,units + 1):
                probability[first][second] = 0.25 * (
                    probability[max(0,first - 4)][second]
                    + probability[max(0,first - 3)][max(0,second - 1)]
                    + probability[max(0,first - 2)][max(0,second - 2)]
                    + probability[first - 1][max(0,second - 3)])
        return probability[units][units]
