from fractions import Fraction


class Solution:
    def judgePoint24(self, cards):
        def possible(values):
            if len(values) == 1:
                return values[0] == 24
            for first in range(len(values)):
                for second in range(first + 1, len(values)):
                    a, b = values[first], values[second]
                    rest = [value for i, value in enumerate(values) if i not in (first, second)]
                    candidates = {a + b, a - b, b - a, a * b}
                    if b:
                        candidates.add(a / b)
                    if a:
                        candidates.add(b / a)
                    for value in candidates:
                        if possible(rest + [value]):
                            return True
            return False

        return possible([Fraction(value) for value in cards])
