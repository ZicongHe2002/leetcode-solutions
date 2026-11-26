class Solution:
    def kthSmallest(self, matrix, k):
        size = len(matrix)
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            middle = (low + high) // 2
            row = size - 1
            count = 0
            for column in range(size):
                while row >= 0 and matrix[row][column] > middle:
                    row -= 1
                count += row + 1
            if count >= k:
                high = middle
            else:
                low = middle + 1
        return low
