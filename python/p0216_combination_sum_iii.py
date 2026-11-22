class Solution:
    def combinationSum3(self, k, n):
        result, path = [], []

        def search(start, remaining):
            needed = k - len(path)
            if needed == 0:
                if remaining == 0:
                    result.append(path[:])
                return
            if start + needed - 1 > 9:
                return
            minimum = needed * (2 * start + needed - 1) // 2
            maximum = needed * (19 - needed) // 2
            if not minimum <= remaining <= maximum:
                return
            for value in range(start, 11 - needed):
                if value > remaining:
                    break
                path.append(value)
                search(value + 1, remaining - value)
                path.pop()

        search(1, n)
        return result
