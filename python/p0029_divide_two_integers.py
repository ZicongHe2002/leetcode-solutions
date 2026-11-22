class Solution:
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        negative = (dividend < 0) != (divisor < 0)
        remaining = dividend if dividend < 0 else -dividend
        block = divisor if divisor < 0 else -divisor
        weight = -1
        while block >= -1073741824 and remaining <= block + block:
            block += block
            weight += weight
        quotient = 0
        while True:
            if remaining <= block:
                remaining -= block
                quotient += weight
            if weight == -1:
                break
            block >>= 1
            weight >>= 1
        return quotient if negative else -quotient
