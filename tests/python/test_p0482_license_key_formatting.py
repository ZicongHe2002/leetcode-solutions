from itertools import product
import unittest

from python.p0482_license_key_formatting import Solution


def reverse_scan_reference(value, width):
    reversed_output = []
    count = 0
    for character in reversed(value):
        if character == '-':
            continue
        if count and count % width == 0:
            reversed_output.append('-')
        reversed_output.append(character.upper())
        count += 1
    return ''.join(reversed(reversed_output))


class LicenseRegroupingTests(unittest.TestCase):
    def check(self, value, width):
        result = Solution().licenseKeyFormatting(value, width)
        self.assertIs(type(result), str)
        self.assertEqual(result, reverse_scan_reference(value, width))
        cleaned = value.replace('-', '').upper()
        self.assertEqual(result.replace('-', ''), cleaned)
        if result:
            groups = result.split('-')
            self.assertTrue(1 <= len(groups[0]) <= width)
            self.assertTrue(all(len(group) == width for group in groups[1:]))

    def test_all_small_keys_and_group_widths_against_reverse_scan(self):
        checks = 0
        for size in range(1, 7):
            for value in product('aB1-', repeat=size):
                for width in range(1, 6):
                    self.check(''.join(value), width)
                    checks += 1
        self.assertEqual(checks, 27300)

    def test_maximum_length_width_and_empty_cleaned_key(self):
        for value in ('aB1-' * 25000, '-' * 100000, 'a' * 100000):
            for width in (1, 3, 10000):
                self.check(value, width)
        self.check('5F3Z-2e-9-w', 4)
        self.check('2-5g-3-J', 2)
        self.check('-', 10000)


if __name__ == '__main__':
    unittest.main()
