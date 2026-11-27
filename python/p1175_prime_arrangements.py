class Solution:
    def numPrimeArrangements(self, n):
        modulus = 10 ** 9 + 7
        prime = [True] * (n + 1)
        prime[0] = False
        prime[1] = False
        for value in range(2, int(n ** 0.5) + 1):
            if prime[value]:
                for multiple in range(value * value, n + 1, value):
                    prime[multiple] = False
        count = sum(prime)
        answer = 1
        for group in (count, n - count):
            for value in range(2, group + 1):
                answer = answer * value % modulus
        return answer
