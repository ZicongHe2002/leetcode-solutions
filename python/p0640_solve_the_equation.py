class Solution:
    def solveEquation(self, equation):
        coefficient = constant = index = 0
        side = 1
        while index < len(equation):
            if equation[index] == '=':
                side = -1
                index += 1
                continue
            sign = side
            if equation[index] in '+-':
                if equation[index] == '-':
                    sign = -sign
                index += 1
            value = 0
            has_digits = False
            while index < len(equation) and equation[index].isdigit():
                value = value * 10 + int(equation[index])
                has_digits = True
                index += 1
            if index < len(equation) and equation[index] == 'x':
                coefficient += sign * (value if has_digits else 1)
                index += 1
            else:
                constant += sign * value
        if coefficient == 0:
            return 'Infinite solutions' if constant == 0 else 'No solution'
        return f'x={-constant // coefficient}'
