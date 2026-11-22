class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return '0'
        negative, value = num < 0, abs(num)
        digits = []
        while value:
            value, remainder = divmod(value, 7)
            digits.append(str(remainder))
        return ('-' if negative else '') + ''.join(reversed(digits))
