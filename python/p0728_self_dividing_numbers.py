class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        for value in range(left, right + 1):
            remaining = value
            while remaining:
                remaining, digit = divmod(remaining, 10)
                if digit == 0 or value % digit:
                    break
            else:
                result.append(value)
        return result
