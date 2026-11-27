class Solution:
    def monotoneIncreasingDigits(self, n):
        digits = [int(char) for char in str(n)]
        suffix = len(digits)
        for index in range(len(digits) - 1, 0, -1):
            if digits[index - 1] > digits[index]:
                digits[index - 1] -= 1
                suffix = index
        for index in range(suffix, len(digits)):
            digits[index] = 9
        return int(''.join(map(str, digits)))
