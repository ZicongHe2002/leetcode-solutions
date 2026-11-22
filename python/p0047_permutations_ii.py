class Solution:
    def permuteUnique(self, nums):
        values = sorted(nums)
        used = [False] * len(values)
        result, path = [], []

        def search():
            if len(path) == len(values):
                result.append(path[:])
                return
            for index, value in enumerate(values):
                if used[index] or (index > 0 and value == values[index - 1] and not used[index - 1]):
                    continue
                used[index] = True
                path.append(value)
                search()
                path.pop()
                used[index] = False

        search()
        return result
