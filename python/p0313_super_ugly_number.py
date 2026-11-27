class Solution:
    def nthSuperUglyNumber(self, n, primes):
        values = [1] * n
        positions = [0] * len(primes)
        candidates = list(primes)
        for index in range(1, n):
            value = min(candidates)
            values[index] = value
            for stream, prime in enumerate(primes):
                if candidates[stream] == value:
                    positions[stream] += 1
                    candidates[stream] = prime * values[positions[stream]]
        return values[-1]
