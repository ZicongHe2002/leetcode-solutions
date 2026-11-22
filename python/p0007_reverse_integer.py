class Solution:
    def reverse(self, x):
        positive = x > 0
        if positive:
            x = -x
        result = 0
        last_minimum = -7 if positive else -8
        while x:
            digit = x % -10
            x = (x - digit) // 10
            if result < -214748364 or (result == -214748364 and digit < last_minimum):
                return 0
            result = result * 10 + digit
        return -result if positive else result
