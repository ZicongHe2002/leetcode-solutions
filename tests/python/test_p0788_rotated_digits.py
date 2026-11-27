import random
import unittest

from python.p0788_rotated_digits import Solution


def actual_text_rotation_prefixes(limit):
    rotation = dict(zip('0182569','0185296'))
    prefix = [0]
    for value in range(1,limit + 1):
        original = str(value)
        try:
            turned = ''.join(rotation[char] for char in original)
        except KeyError:
            turned = None
        prefix.append(prefix[-1] + (turned is not None and turned != original))
    return prefix


class RotatedDigitsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected = actual_text_rotation_prefixes(10000)

    def check(self, n, expected=None):
        result = Solution().rotatedDigits(n)
        self.assertIs(type(result),int)
        self.assertEqual(result,self.expected[n] if expected is None else expected,n)

    def test_every_small_upper_bound_against_full_literal_text_rotation_counts(self):
        for n in range(1,501):
            self.check(n)

    def test_seeded_upper_bounds_official_examples_maximum_and_digit_length_closed_forms(self):
        rng = random.Random(788)
        for _ in range(100):
            self.check(rng.randrange(1,10001))
        self.check(1,0)
        self.check(2,1)
        self.check(10,4)
        self.check(69)
        for digits in range(1,5):
            self.check(10**digits - 1,7**digits - 3**digits)
        self.check(10000,2320)


if __name__ == '__main__':
    unittest.main()
