class Solution:
    def calculate(self, s):
        total = number = 0
        sign = 1
        contexts = []
        for character in s:
            if character.isdigit():
                number = number * 10 + int(character)
            elif character in '+-':
                total += sign * number
                number = 0
                sign = 1 if character == '+' else -1
            elif character == '(':
                contexts.append((total, sign))
                total = number = 0
                sign = 1
            elif character == ')':
                total += sign * number
                number = 0
                outer_total, outer_sign = contexts.pop()
                total = outer_total + outer_sign * total
                sign = 1
        return total + sign * number
