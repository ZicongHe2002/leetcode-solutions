class Solution:
    def flipAndInvertImage(self, image):
        return [[1 - value for value in row[::-1]] for row in image]
