import unittest
from collections import Counter
from itertools import product

from python.p0726_number_of_atoms import Solution


def atom(name, count):
    return name + (str(count) if count > 1 else ''), Counter({name: count})


def concatenate(left, right):
    return left[0] + right[0], left[1] + right[1]


def group(child, count):
    return '(' + child[0] + ')' + (str(count) if count > 1 else ''), Counter({name: amount * count for name, amount in child[1].items()})


def render(counts):
    return ''.join(name + (str(counts[name]) if counts[name] > 1 else '') for name in sorted(counts))


class NumberOfAtomsTests(unittest.TestCase):
    def check(self, formula, expected):
        result = Solution().countOfAtoms(formula)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected, formula)

    def test_all_constructed_component_pairs_and_group_multipliers(self):
        atoms = [atom(name, count) for name in ('H', 'He', 'Mg', 'O') for count in (1, 2, 12)]
        components = atoms + [concatenate(a, b) for a, b in product(atoms, repeat=2)]
        components += [group(a, count) for a in atoms for count in (1, 2, 3, 12)]
        self.assertEqual(len(components), 204)
        checked = 0
        for a, b in product(components, repeat=2):
            formula, counts = concatenate(a, b)
            self.check(formula, render(counts))
            checked += 1
        for a in components:
            for count in (1, 2, 3):
                formula, counts = group(a, count)
                self.check(formula, render(counts))
                checked += 1
        self.assertEqual(checked, 42228)

    def test_examples_deep_thousand_character_formulas_and_integer_boundary(self):
        for formula, expected in (('H2O', 'H2O'), ('Mg(OH)2', 'H2MgO2'),
                                  ('K4(ON(SO3)2)2', 'K4N2O14S4'),
                                  ('HeHHeH', 'H2He2'), ('H2147483647', 'H2147483647')):
            self.check(formula, expected)
        formula = '(' * 499 + 'He' + ')' * 499
        self.assertEqual(len(formula), 1000)
        self.check(formula, 'He')
        formula = '(' * 498 + 'H2' + ')' * 498 + '12'
        self.assertEqual(len(formula), 1000)
        self.check(formula, 'H24')
        self.check('H' * 1000, 'H1000')


if __name__ == '__main__':
    unittest.main()
