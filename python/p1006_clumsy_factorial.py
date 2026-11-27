class Solution:
    def clumsy(self, n):
        terms = [n]
        operation = 0
        for value in range(n - 1,0,-1):
            if operation == 0:
                terms[-1] *= value
            elif operation == 1:
                numerator = terms[-1]
                terms[-1] = numerator // value if numerator >= 0 else -((-numerator) // value)
            elif operation == 2:
                terms.append(value)
            else:
                terms.append(-value)
            operation = (operation + 1) % 4
        return sum(terms)
