from itertools import groupby, product
import unittest

from python.p0925_long_pressed_name import Solution


def run_lengths_reference(name, typed):
    groups = lambda value: [(character, len(list(run))) for character, run in groupby(value)]
    original, actual = groups(name), groups(typed)
    return len(original) == len(actual) and all(
        left == right and count <= repeated
        for (left, count), (right, repeated) in zip(original, actual))


class LongPressPrefixTests(unittest.TestCase):
    def check(self, name, typed):
        result = Solution().isLongPressedName(name, typed)
        self.assertIs(type(result), bool)
        self.assertEqual(result, run_lengths_reference(name, typed))

    def test_all_small_name_and_typed_pairs_against_run_lengths(self):
        names = [''.join(chars) for size in range(1, 5) for chars in product('abc', repeat=size)]
        typed_strings = [''.join(chars) for size in range(1, 6) for chars in product('abc', repeat=size)]
        checks = 0
        for name in names:
            for typed in typed_strings:
                self.check(name, typed)
                checks += 1
        self.assertEqual(checks, 43560)

    def test_maximum_lengths_suffixes_and_missing_original_characters(self):
        self.check('a', 'a' * 1000)
        self.check('a' * 1000, 'a' * 999)
        self.check('ab' * 500, 'ab' * 500)
        self.check('alex', 'aaleex')
        self.check('saeed', 'ssaaedd')
        self.check('alex', 'alexx')
        self.check('alex', 'alexz')
        self.check('aabb', 'abbb')
        self.check('ab', 'a' * 999 + 'b')


if __name__ == '__main__':
    unittest.main()
