class Solution:
    def calculate(self, s):
        values, operators = [], []
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, 'u+': 3, 'u-': 3}

        def apply():
            operator = operators.pop()
            if operator in ('u+', 'u-'):
                values[-1] *= 1 if operator == 'u+' else -1
                return
            right, left = values.pop(), values.pop()
            if operator == '+':
                result = left + right
            elif operator == '-':
                result = left - right
            elif operator == '*':
                result = left * right
            else:
                magnitude = abs(left) // abs(right)
                result = -magnitude if (left < 0) != (right < 0) else magnitude
            values.append(result)

        index, expecting_operand = 0, True
        while index < len(s):
            char = s[index]
            if char == ' ':
                index += 1
                continue
            if char.isdigit():
                value = 0
                while index < len(s) and s[index].isdigit():
                    value = 10 * value + int(s[index])
                    index += 1
                values.append(value)
                while operators and operators[-1] in ('u+', 'u-'):
                    apply()
                expecting_operand = False
                continue
            if char == '(':
                operators.append(char)
                expecting_operand = True
            elif char == ')':
                while operators[-1] != '(':
                    apply()
                operators.pop()
                while operators and operators[-1] in ('u+', 'u-'):
                    apply()
                expecting_operand = False
            elif expecting_operand and char in ('+', '-'):
                operators.append('u' + char)
            else:
                while operators and operators[-1] != '(' and priority[operators[-1]] >= priority[char]:
                    apply()
                operators.append(char)
                expecting_operand = True
            index += 1
        while operators:
            apply()
        return values[0]
