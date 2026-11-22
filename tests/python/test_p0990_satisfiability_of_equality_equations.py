from itertools import product
import unittest

from python.p0990_satisfiability_of_equality_equations import Solution


def explicit_assignments(equations):
    for values in product(range(3), repeat=3):
        assignment = dict(zip('abc', values))
        if all((assignment[equation[0]] == assignment[equation[3]]) == (equation[1] == '=')
               for equation in equations):
            return True
    return False


class EqualityAssignmentTests(unittest.TestCase):
    def check(self, equations, expected=None):
        before = equations[:]
        if expected is None:
            expected = explicit_assignments(equations)
        result = Solution().equationsPossible(equations)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(equations, before)

    def test_all_small_relation_sequences_against_assignments(self):
        relations = ('a==a', 'a!=a', 'a==b', 'a!=b', 'b==c', 'b!=c', 'a==c', 'a!=c')
        checks = 0
        for length in range(1, 5):
            for equations in product(relations, repeat=length):
                self.check(list(equations))
                checks += 1
        self.assertEqual(checks, 4680)

    def test_maximum_relations_all_letters_transitivity_and_self_constraints(self):
        for length, expected in ((25, False), (24, True)):
            equations = [chr(97 + index) + '==' + chr(98 + index) for index in range(length)]
            equations += ['a!=z']
            equations += ['a==a'] * (500 - len(equations))
            self.check(equations, expected)
        self.check(['a==a'] * 500, True)
        self.check(['z!=z'] * 500, False)


if __name__ == '__main__':
    unittest.main()
