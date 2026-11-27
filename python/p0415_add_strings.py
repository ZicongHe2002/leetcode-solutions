class Solution:
    def addStrings(self, num1, num2):
        left, right = len(num1) - 1, len(num2) - 1
        carry = 0
        digits = []
        while left >= 0 or right >= 0 or carry:
            total = carry
            if left >= 0:
                total += ord(num1[left]) - ord('0')
                left -= 1
            if right >= 0:
                total += ord(num2[right]) - ord('0')
                right -= 1
            carry, digit = divmod(total, 10)
            digits.append(chr(ord('0') + digit))
        digits.reverse()
        return ''.join(digits)
