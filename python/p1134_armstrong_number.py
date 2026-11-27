class Solution:
    def isArmstrong(self, n):
        digits = str(n)
        power = len(digits)
        return sum(int(digit) ** power for digit in digits) == n
