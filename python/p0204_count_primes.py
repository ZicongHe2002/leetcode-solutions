from math import isqrt


class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        prime = bytearray([1]) * n
        prime[0] = prime[1] = 0
        for value in range(2, isqrt(n - 1) + 1):
            if prime[value]:
                start = value * value
                prime[start:n:value] = bytes((n - 1 - start) // value + 1)
        return sum(prime)
