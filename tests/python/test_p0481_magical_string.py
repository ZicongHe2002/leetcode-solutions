from itertools import groupby, product
import unittest

from python.p0481_magical_string import Solution


def exhaustive_self_describing_prefix(length):
    seed = (1, 2, 2)[:length]
    valid = []
    for tail in product((1, 2), repeat=max(0, length - 3)):
        candidate = seed + tail
        runs = [len(list(group)) for _, group in groupby(candidate)]
        if runs[:-1] == list(candidate[:len(runs) - 1]) and runs[-1] <= candidate[len(runs) - 1]:
            valid.append(candidate)
    if len(valid) != 1:
        raise AssertionError(('prefix must be unique', length, valid))
    return valid[0]


def global_run_expansion(length):
    prefix = '122'
    while len(prefix) < length:
        expanded = ''.join(('1' if index % 2 == 0 else '2') * int(count)
                           for index, count in enumerate(prefix))
        if not expanded.startswith(prefix) or len(expanded) <= len(prefix):
            raise AssertionError('whole expansions must form growing nested prefixes')
        prefix = expanded
    return prefix[:length]


class SelfDescribingRunTests(unittest.TestCase):
    def test_all_short_seed_extensions_have_one_valid_prefix(self):
        for n in range(1, 19):
            reference = exhaustive_self_describing_prefix(n)
            self.assertEqual(Solution().magicalString(n), reference.count(1))
        self.assertEqual(Solution().magicalString(0), 0)

    def test_all_first_thousand_prefix_counts_and_maximum_against_global_expansion(self):
        reference = global_run_expansion(100000)
        ones = 0
        for n, digit in enumerate(reference[:1000], 1):
            ones += digit == '1'
            actual = Solution().magicalString(n)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, ones)
        for n in (99999, 100000):
            self.assertEqual(Solution().magicalString(n), reference[:n].count('1'))
        self.assertEqual(Solution().magicalString(6), 3)


if __name__ == '__main__':
    unittest.main()
