class Solution:
    def evaluate(self, expression):
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        position = 0
        values = {}

        def parse():
            nonlocal position
            token = tokens[position]
            position += 1
            if token != '(':
                return values[token][-1] if token[0].islower() else int(token)
            operation = tokens[position]
            position += 1
            if operation in ('add', 'mult'):
                left, right = parse(), parse()
                position += 1
                return left + right if operation == 'add' else left * right
            assigned = []
            while True:
                token = tokens[position]
                if token == '(' or token[0] == '-' or token[0].isdigit() or tokens[position + 1] == ')':
                    result = parse()
                    break
                position += 1
                value = parse()
                values.setdefault(token, []).append(value)
                assigned.append(token)
            position += 1
            for name in reversed(assigned):
                values[name].pop()
                if not values[name]:
                    del values[name]
            return result

        return parse()
