class Solution:
    def numRollsToTarget(self, n, k, target):
        modulus = 10 ** 9 + 7
        previous = [0] * (target + 1)
        previous[0] = 1
        for _ in range(n):
            current = [0] * (target + 1)
            window = 0
            for total in range(1, target + 1):
                window += previous[total - 1]
                if total - k - 1 >= 0:
                    window -= previous[total - k - 1]
                window %= modulus
                current[total] = window
            previous = current
        return previous[target]
