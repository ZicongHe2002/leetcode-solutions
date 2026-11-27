class Solution:
    def toHex(self, num):
        if num == 0:
            return '0'
        value = num & 0xffffffff
        digits, alphabet = [], '0123456789abcdef'
        while value:
            digits.append(alphabet[value & 15])
            value >>= 4
        return ''.join(reversed(digits))
