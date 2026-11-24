class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        columns = len(matrix[0])
        left, right = 0, len(matrix) * columns
        while left < right:
            middle = left + (right - left) // 2
            value = matrix[middle // columns][middle % columns]
            if value == target:
                return True
            if value < target:
                left = middle + 1
            else:
                right = middle
        return False
