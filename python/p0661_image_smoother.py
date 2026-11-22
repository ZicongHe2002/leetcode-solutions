class Solution:
    def imageSmoother(self, img):
        rows, columns = len(img), len(img[0])
        output = [[0] * columns for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                total = count = 0
                for nearby_row in range(max(0, row - 1), min(rows, row + 2)):
                    for nearby_column in range(max(0, column - 1), min(columns, column + 2)):
                        total += img[nearby_row][nearby_column]
                        count += 1
                output[row][column] = total // count
        return output
