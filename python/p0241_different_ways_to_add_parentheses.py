from functools import lru_cache


class Solution:
    def diffWaysToCompute(self, expression):
        @lru_cache(None)
        def evaluate(start, end):
            results = []
            for index in range(start, end):
                operator = expression[index]
                if operator not in '+-*':
                    continue
                for left in evaluate(start, index):
                    for right in evaluate(index + 1, end):
                        if operator == '+':
                            results.append(left + right)
                        elif operator == '-':
                            results.append(left - right)
                        else:
                            results.append(left * right)
            return tuple(results) if results else (int(expression[start:end]),)

        return list(evaluate(0, len(expression)))
