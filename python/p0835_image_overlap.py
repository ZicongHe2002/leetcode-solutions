from collections import Counter


class Solution:
    def largestOverlap(self, img1, img2):
        first = [(row,column) for row,values in enumerate(img1) for column,value in enumerate(values) if value]
        second = [(row,column) for row,values in enumerate(img2) for column,value in enumerate(values) if value]
        translations = Counter()
        for first_row,first_column in first:
            for second_row,second_column in second:
                translations[second_row - first_row,second_column - first_column] += 1
        return max(translations.values(),default=0)
