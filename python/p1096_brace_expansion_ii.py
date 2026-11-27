class Solution:
    def braceExpansionII(self, expression):
        index = 0

        def parse_expression():
            nonlocal index
            union = set()
            product = {''}
            while index < len(expression) and expression[index] != '}':
                token = expression[index]
                if token == ',':
                    union.update(product)
                    product = {''}
                    index += 1
                    continue
                if token == '{':
                    index += 1
                    choices = parse_expression()
                    index += 1
                else:
                    choices = {token}
                    index += 1
                product = {prefix + suffix for prefix in product for suffix in choices}
            union.update(product)
            return union

        return sorted(parse_expression())
