class Solution:
    def isNumber(self, s):
        digit = False
        decimal = False
        exponent = False
        for index, character in enumerate(s):
            if '0' <= character <= '9':
                digit = True
            elif character in '+-':
                if index != 0 and s[index - 1] not in 'eE':
                    return False
            elif character == '.':
                if decimal or exponent:
                    return False
                decimal = True
            elif character in 'eE':
                if exponent or not digit:
                    return False
                exponent = True
                digit = False
            else:
                return False
        return digit
