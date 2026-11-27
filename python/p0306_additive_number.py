class Solution:
    def isAdditiveNumber(self, num):
        def add_decimal(first, second):
            left, right = len(first) - 1, len(second) - 1
            carry = 0
            digits = []
            while left >= 0 or right >= 0 or carry:
                total = carry
                if left >= 0:
                    total += ord(first[left]) - ord('0')
                    left -= 1
                if right >= 0:
                    total += ord(second[right]) - ord('0')
                    right -= 1
                carry, digit = divmod(total, 10)
                digits.append(chr(ord('0') + digit))
            return ''.join(reversed(digits))

        for first_end in range(1, len(num) - 1):
            if first_end > 1 and num[0] == '0':
                break
            for second_end in range(first_end + 1, len(num)):
                if second_end > first_end + 1 and num[first_end] == '0':
                    break
                first, second = num[:first_end], num[first_end:second_end]
                position = second_end
                while position < len(num):
                    following = add_decimal(first, second)
                    if not num.startswith(following, position):
                        break
                    position += len(following)
                    first, second = second, following
                if position == len(num):
                    return True
        return False
