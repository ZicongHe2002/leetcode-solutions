class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        sign = '-' if (numerator < 0) != (denominator < 0) else ''
        whole, remainder = divmod(abs(numerator), abs(denominator))
        prefix = sign + str(whole)
        if remainder == 0:
            return prefix
        prefix += '.'
        denominator = abs(denominator)
        digits, positions = [], {}
        while remainder:
            if remainder in positions:
                begin = positions[remainder]
                return prefix + ''.join(digits[:begin]) + '(' + ''.join(digits[begin:]) + ')'
            positions[remainder] = len(digits)
            digit, remainder = divmod(remainder * 10, denominator)
            digits.append(str(digit))
        return prefix + ''.join(digits)
