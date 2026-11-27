class Solution:
    def powerfulIntegers(self, x, y, bound):
        def powers(base):
            values = [1]
            if base != 1:
                while values[-1] * base <= bound:
                    values.append(values[-1] * base)
            return values

        return list({first + second for first in powers(x) for second in powers(y)
                     if first + second <= bound})
