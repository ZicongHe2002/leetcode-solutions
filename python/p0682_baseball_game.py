class Solution:
    def calPoints(self, operations):
        scores = []
        for operation in operations:
            if operation == 'C':
                scores.pop()
            elif operation == 'D':
                scores.append(2 * scores[-1])
            elif operation == '+':
                scores.append(scores[-2] + scores[-1])
            else:
                scores.append(int(operation))
        return sum(scores)
