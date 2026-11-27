class Solution:
    def kInversePairs(self, n, k):
        if k > n * (n - 1) // 2:
            return 0
        modulus = 10**9 + 7
        previous = [1] + [0] * k
        for size in range(2, n + 1):
            current = [0] * (k + 1)
            window = 0
            for inversions in range(min(k, size * (size - 1) // 2) + 1):
                window += previous[inversions]
                if inversions >= size:
                    window -= previous[inversions - size]
                window %= modulus
                current[inversions] = window
            previous = current
        return previous[k]
