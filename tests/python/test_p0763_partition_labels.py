import string
import unittest
from itertools import product

from python.p0763_partition_labels import Solution


def all_cuts_oracle(text):
    if not text:
        return []
    best = []
    for mask in range(1 << (len(text) - 1)):
        cuts = [0] + [index + 1 for index in range(len(text) - 1) if mask & (1 << index)] + [len(text)]
        owners = {}
        lengths = []
        valid = True
        for group, (left, right) in enumerate(zip(cuts, cuts[1:])):
            for letter in text[left:right]:
                if letter in owners and owners[letter] != group:
                    valid = False
                    break
                owners[letter] = group
            if not valid:
                break
            lengths.append(right - left)
        if valid and len(lengths) > len(best):
            best = lengths
    return best


class PartitionLabelTests(unittest.TestCase):
    def test_all_small_ternary_strings_against_all_cut_masks(self):
        checks = 0
        for size in range(8):
            for letters in product('abc', repeat=size):
                text = ''.join(letters)
                self.assertEqual(Solution().partitionLabels(text), all_cuts_oracle(text))
                checks += 1
        self.assertEqual(checks, 3280)

    def test_examples_maximum_length_and_maximum_partition_count(self):
        cases = [('ababcbacadefegdehijhklij', [9, 7, 8]), ('eccbbbbdec', [10]),
                 ('abac', [3, 1]), ('a' * 500, [500]), (string.ascii_lowercase, [1] * 26),
                 ('a' * 475 + string.ascii_lowercase[1:], [475] + [1] * 25), ('', [])]
        for text, expected in cases:
            self.assertEqual(Solution().partitionLabels(text), expected)


if __name__ == '__main__':
    unittest.main()
