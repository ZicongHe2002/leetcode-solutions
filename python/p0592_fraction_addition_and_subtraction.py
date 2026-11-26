from math import gcd


class Solution:
    def fractionAddition(self, expression):
        numerator, denominator = 0, 1
        index = 0
        while index < len(expression):
            sign = 1
            if expression[index] in '+-':
                if expression[index] == '-':
                    sign = -1
                index += 1
            slash = expression.index('/', index)
            term_numerator = sign * int(expression[index:slash])
            end = slash + 1
            while end < len(expression) and expression[end].isdigit():
                end += 1
            term_denominator = int(expression[slash + 1:end])
            numerator = numerator * term_denominator + term_numerator * denominator
            denominator *= term_denominator
            divisor = gcd(abs(numerator), denominator)
            numerator //= divisor
            denominator //= divisor
            index = end
        return f'{numerator}/{denominator}'
