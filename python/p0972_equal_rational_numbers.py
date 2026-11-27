from fractions import Fraction


class Solution:
    def isRationalEqual(self, s, t):
        def value(text):
            repeating = ''
            if '(' in text:
                text,repeating = text[:-1].split('(')
            if '.' in text:
                integer,decimal = text.split('.',1)
            else:
                integer,decimal = text,''
            result = Fraction(int(integer),1)
            scale = 10**len(decimal)
            if decimal:
                result += Fraction(int(decimal),scale)
            if repeating:
                result += Fraction(int(repeating),scale * (10**len(repeating) - 1))
            return result

        return value(s) == value(t)
