class Solution:
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        frequencies = []
        for row in range(sideLength):
            row_count = (height - 1 - row) // sideLength + 1
            for column in range(sideLength):
                column_count = (width - 1 - column) // sideLength + 1
                frequencies.append(row_count * column_count)
        frequencies.sort(reverse=True)
        return sum(frequencies[:maxOnes])
