class Solution:
    def findDerangement(self, n):
        previous, current = 1, 0
        modulus = 10**9 + 7
        for size in range(2, n + 1):
            previous, current = current, (size - 1) * (previous + current) % modulus
        return current
