class Solution:
    def ambiguousCoordinates(self, s):
        digits = s[1:-1]

        def forms(text):
            result = []
            if len(text) == 1 or text[0] != '0':
                result.append(text)
            if text[-1] != '0':
                for split in range(1,len(text)):
                    integer = text[:split]
                    if len(integer) == 1 or integer[0] != '0':
                        result.append(integer + '.' + text[split:])
            return result

        result = []
        for split in range(1,len(digits)):
            left,right = forms(digits[:split]),forms(digits[split:])
            result.extend('(' + first + ', ' + second + ')' for first in left for second in right)
        return result
