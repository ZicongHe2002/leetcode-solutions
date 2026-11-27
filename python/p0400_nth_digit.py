class Solution:
    def findNthDigit(self, n):
        width = 1
        first = 1
        count = 9
        while n > width * count:
            n -= width * count
            width += 1
            first *= 10
            count *= 10
        number = first + (n - 1) // width
        offset = (n - 1) % width
        return (number // (10 ** (width - offset - 1))) % 10
