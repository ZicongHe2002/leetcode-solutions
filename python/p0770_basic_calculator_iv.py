import re


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        bindings = dict(zip(evalvars, evalints))
        tokens = re.findall(r'[a-z]+|[0-9]+|[()+*-]', expression)
        cursor = 0

        def add(left, right, sign):
            result = left.copy()
            for term, coefficient in right.items():
                value = result.get(term, 0) + sign * coefficient
                if value:
                    result[term] = value
                else:
                    result.pop(term, None)
            return result

        def multiply(left, right):
            result = {}
            for first, a in left.items():
                for second, b in right.items():
                    term = tuple(sorted(first + second))
                    result[term] = result.get(term, 0) + a * b
            return {term: value for term, value in result.items() if value}

        def factor():
            nonlocal cursor
            token = tokens[cursor]
            cursor += 1
            if token == '(':
                result = expression_sum()
                cursor += 1
                return result
            if token.isdigit() or token in bindings:
                value = int(token) if token.isdigit() else bindings[token]
                return {(): value} if value else {}
            return {(token,): 1}

        def expression_product():
            nonlocal cursor
            result = factor()
            while cursor < len(tokens) and tokens[cursor] == '*':
                cursor += 1
                result = multiply(result, factor())
            return result

        def expression_sum():
            nonlocal cursor
            result = expression_product()
            while cursor < len(tokens) and tokens[cursor] in ('+', '-'):
                operator = tokens[cursor]
                cursor += 1
                result = add(result, expression_product(), 1 if operator == '+' else -1)
            return result

        polynomial = expression_sum()
        return [str(polynomial[term]) + ''.join('*' + variable for variable in term)
                for term in sorted(polynomial, key=lambda term: (-len(term), term))]
