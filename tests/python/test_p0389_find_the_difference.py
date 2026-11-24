import unittest
from collections import Counter
from itertools import product

from python.p0389_find_the_difference import Solution


def unique_orders(counts, length, prefix=()):
    if len(prefix) == length:
        yield ''.join(prefix)
        return
    for character in counts:
        if counts[character]:
            counts[character] -= 1
            yield from unique_orders(counts, length, prefix + (character,))
            counts[character] += 1


class DifferenceTests(unittest.TestCase):
    def check(self, source, target):
        extra = list((Counter(target) - Counter(source)).elements())
        self.assertEqual(len(extra), 1)
        result = Solution().findTheDifference(source, target)
        self.assertIs(type(result), str)
        self.assertEqual(result, extra[0])
        self.assertEqual(len(result), 1)

    def test_all_small_sources_added_letters_and_unique_target_orders_against_counter(self):
        checks = 0
        for size in range(7):
            for letters in product('ab', repeat=size):
                source = ''.join(letters)
                for added in 'abc':
                    for target in unique_orders(Counter(source + added), size + 1):
                        self.check(source, target)
                        checks += 1
        self.assertEqual(checks, 13139)

    def test_maximum_length_existing_extra_repetition_and_empty_source(self):
        self.check('a' * 1000, 'a' * 1000 + 'z')
        self.check('a' * 500 + 'b' * 500, 'b' * 501 + 'a' * 500)
        self.check('z' * 1000, 'z' * 1001)
        self.check('', 'a')


if __name__ == '__main__':
    unittest.main()
