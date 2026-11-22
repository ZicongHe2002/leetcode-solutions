import unittest
from itertools import combinations, product

from python.p0093_restore_ip_addresses import Solution


def all_three_cut_positions(word):
    result = set()
    for cuts in combinations(range(1, len(word)), 3):
        edges = (0, *cuts, len(word))
        parts = [word[edges[i]:edges[i + 1]] for i in range(4)]
        if all(1 <= len(part) <= 3 and (len(part) == 1 or part[0] != '0') and int(part) <= 255 for part in parts):
            result.add('.'.join(parts))
    return result


class RestoredIpTests(unittest.TestCase):
    def check(self, word, expected=None):
        if expected is None:
            expected = all_three_cut_positions(word)
        result = Solution().restoreIpAddresses(word)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(address) is str for address in result))
        self.assertEqual(len(result), len(set(result)))
        self.assertEqual(set(result), set(expected))

    def test_all_small_digit_strings_against_all_three_cuts(self):
        checks = 0
        for size in range(9):
            for digits in product('012', repeat=size):
                self.check(''.join(digits))
                checks += 1
        self.assertEqual(checks, 9841)

    def test_maximum_length_segment_bounds_zeros_and_multiple_addresses(self):
        self.check('1' * 20, [])
        self.check('255255255255', ['255.255.255.255'])
        self.check('256256256256', [])
        self.check('0000', ['0.0.0.0'])
        self.check('1111', ['1.1.1.1'])
        self.check('101023', ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3'])
        self.check('25525511135', ['255.255.11.135', '255.255.111.35'])


if __name__ == '__main__':
    unittest.main()
