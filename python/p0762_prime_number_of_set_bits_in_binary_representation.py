class Solution:
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(value.bit_count() in primes for value in range(left, right + 1))
