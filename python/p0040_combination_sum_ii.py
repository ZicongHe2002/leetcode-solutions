class Solution:
    def combinationSum2(self, candidates, target):
        values = sorted(candidates)
        result = []
        path = []

        def visit(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for index in range(start, len(values)):
                if index > start and values[index] == values[index - 1]:
                    continue
                value = values[index]
                if value > remaining:
                    break
                path.append(value)
                visit(index + 1, remaining - value)
                path.pop()

        visit(0, target)
        return result
