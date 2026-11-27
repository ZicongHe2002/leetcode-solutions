class Solution:
    def calculate(self, s):
        total = term = number = 0
        previous = '+'
        for index, character in enumerate(s):
            if character.isdigit():
                number = number * 10 + int(character)
            if character in '+-*/' or index == len(s) - 1:
                if previous == '+':
                    total += term
                    term = number
                elif previous == '-':
                    total += term
                    term = -number
                elif previous == '*':
                    term *= number
                else:
                    term = (abs(term) // number) * (1 if term >= 0 else -1)
                previous = character
                number = 0
        return total + term
