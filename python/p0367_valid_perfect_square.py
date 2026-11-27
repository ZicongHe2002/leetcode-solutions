class Solution:
    def isPerfectSquare(self, num):
        low, high = 1, num
        while low <= high:
            middle = (low + high) // 2
            square = middle * middle
            if square == num:
                return True
            if square < num:
                low = middle + 1
            else:
                high = middle - 1
        return False
