class Solution:
    def beautifulArray(self, n):
        result = [1]
        while len(result) < n:
            result = [2 * value - 1 for value in result if 2 * value - 1 <= n] + [
                2 * value for value in result if 2 * value <= n]
        return result
