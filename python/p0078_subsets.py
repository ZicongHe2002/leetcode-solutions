class Solution:
    def subsets(self, nums):
        result = []
        path = []

        def visit(start):
            result.append(path[:])
            for index in range(start, len(nums)):
                path.append(nums[index])
                visit(index + 1)
                path.pop()

        visit(0)
        return result
