class Solution:
    def permute(self, nums):
        result = []
        path = []
        used = [False] * len(nums)

        def visit():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for index, value in enumerate(nums):
                if used[index]:
                    continue
                used[index] = True
                path.append(value)
                visit()
                path.pop()
                used[index] = False

        visit()
        return result
