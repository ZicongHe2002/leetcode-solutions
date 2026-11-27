class Solution:
    def superPow(self, a, b):
        modulus = 1337
        base = a % modulus
        result = 1
        for digit in b:
            result = pow(result, 10, modulus) * pow(base, digit, modulus) % modulus
        return result
