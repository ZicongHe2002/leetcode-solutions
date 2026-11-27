class Solution:
    def countNumbersWithUniqueDigits(self, n):
        total = 1
        ways = 9
        for digits in range(1, n + 1):
            total += ways
            ways *= 10 - digits
        return total
