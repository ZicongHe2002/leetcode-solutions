from collections import Counter


class Solution:
    def findBlackPixel(self, picture, target):
        patterns = Counter(tuple(row) for row in picture)
        column_black = [sum(row[column] == 'B' for row in picture)
                        for column in range(len(picture[0]))]
        answer = 0
        for pattern, frequency in patterns.items():
            if frequency != target or pattern.count('B') != target:
                continue
            answer += target * sum(pixel == 'B' and column_black[column] == target
                                   for column, pixel in enumerate(pattern))
        return answer
