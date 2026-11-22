class Solution:
    def subsetsWithDup(self, nums):
        values = sorted(nums)
        result = []
        path = []

        def visit(start):
            result.append(path[:])
            for index in range(start, len(values)):
                if index > start and values[index] == values[index - 1]:
                    continue
                path.append(values[index])
                visit(index + 1)
                path.pop()

        visit(0)
        return result
