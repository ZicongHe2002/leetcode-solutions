class Solution:
    def rotatedDigits(self, n):
        total = 0
        for value in range(1,n + 1):
            changed = False
            while value:
                digit = value % 10
                if digit in (3,4,7):
                    break
                if digit in (2,5,6,9):
                    changed = True
                value //= 10
            else:
                total += changed
        return total
