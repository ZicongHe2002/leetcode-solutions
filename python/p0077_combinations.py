class Solution:
    def combine(self, n, k):
        result, path = [], []

        def search(start):
            if len(path) == k:
                result.append(path[:])
                return
            remaining = k - len(path)
            for value in range(start, n - remaining + 2):
                path.append(value)
                search(value + 1)
                path.pop()

        search(1)
        return result
