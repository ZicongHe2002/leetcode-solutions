import re
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula):
        tokens = re.findall(r'[A-Z][a-z]*|[0-9]+|[()]', formula)
        totals = defaultdict(int)
        multipliers = [1]
        count = 1
        for token in reversed(tokens):
            if token[0].isdigit():
                count = int(token)
            elif token == ')':
                multipliers.append(multipliers[-1] * count)
                count = 1
            elif token == '(':
                multipliers.pop()
            else:
                totals[token] += multipliers[-1] * count
                count = 1
        return ''.join(atom + (str(totals[atom]) if totals[atom] > 1 else '')
                       for atom in sorted(totals))
