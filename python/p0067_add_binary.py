class Solution:
    def addBinary(self, a, b):
        first, second = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while first >= 0 or second >= 0 or carry:
            left = ord(a[first]) - ord('0') if first >= 0 else 0
            right = ord(b[second]) - ord('0') if second >= 0 else 0
            carry, bit = divmod(left + right + carry, 2)
            result.append(str(bit))
            first -= 1
            second -= 1
        return ''.join(reversed(result))
