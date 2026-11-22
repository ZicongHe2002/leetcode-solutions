class Solution:
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        digits = [0] * (len(num1) + len(num2))
        for first, left in enumerate(reversed(num1)):
            for second, right in enumerate(reversed(num2)):
                digits[first + second] += (ord(left) - ord('0')) * (ord(right) - ord('0'))
        for index in range(len(digits) - 1):
            carry, digits[index] = divmod(digits[index], 10)
            digits[index + 1] += carry
        while len(digits) > 1 and digits[-1] == 0:
            digits.pop()
        return ''.join(str(digit) for digit in reversed(digits))
