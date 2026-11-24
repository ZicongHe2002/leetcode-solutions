class Solution:
    def evalRPN(self, tokens):
        values = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                values.append(int(token))
                continue
            right, left = values.pop(), values.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            else:
                magnitude = abs(left) // abs(right)
                result = -magnitude if (left < 0) != (right < 0) else magnitude
            values.append(result)
        return values[-1]
