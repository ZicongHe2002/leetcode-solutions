class Solution:
    def getPermutation(self, n, k):
        factorials = [1] * (n + 1)
        for value in range(1, n + 1):
            factorials[value] = factorials[value - 1] * value
        available = [str(value) for value in range(1, n + 1)]
        result = []
        k -= 1
        for remaining in range(n, 0, -1):
            index, k = divmod(k, factorials[remaining - 1])
            result.append(available.pop(index))
        return ''.join(result)
