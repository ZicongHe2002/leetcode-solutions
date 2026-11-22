from itertools import product
import unittest

from python.p0796_rotate_string import Solution


def shifted_states_reference(value, goal):
    states = set()
    for _ in range(len(value)):
        states.add(value)
        value = value[1:] + value[0]
    return goal in states


class RotationKMPTests(unittest.TestCase):
    def check(self, value, goal):
        result = Solution().rotateString(value, goal)
        self.assertIs(type(result), bool)
        self.assertEqual(result, shifted_states_reference(value, goal))

    def test_all_small_string_pairs_against_shifted_states(self):
        strings = [''.join(chars) for size in range(1, 7)
                   for chars in product('ab', repeat=size)]
        checks = 0
        for value in strings:
            for goal in strings:
                self.check(value, goal)
                checks += 1
        self.assertEqual(checks, 15876)

    def test_maximum_length_periodic_prefixes_and_all_rotations(self):
        value = 'a' * 48 + 'ba' + 'a' * 49 + 'c'
        self.assertEqual(len(value), 100)
        for index in range(100):
            self.check(value, value[index:] + value[:index])
        self.check('ab' * 50, 'ba' * 50)
        self.check('a' * 100, 'a' * 99 + 'b')
        self.check('abcde', 'abced')
        self.check('a', 'aa')


if __name__ == '__main__':
    unittest.main()
