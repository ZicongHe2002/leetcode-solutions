from itertools import product
import unittest

from python.p0541_reverse_string_ii import Solution


def source_index_mapping_oracle(text, k):
    output = []
    for index in range(len(text)):
        block = index // (2 * k) * (2 * k)
        offset = index - block
        reversed_length = min(k, len(text) - block)
        source = block + reversed_length - 1 - offset if offset < reversed_length else index
        output.append(text[source])
    return ''.join(output)


class AlternatingPrefixReverseTests(unittest.TestCase):
    def check(self, text, k, expected=None):
        actual = Solution().reverseStr(text, k)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, source_index_mapping_oracle(text, k) if expected is None else expected)
        self.assertEqual(len(actual), len(text))

    def test_every_short_string_and_block_size_against_source_indices(self):
        strings = queries = 0
        for size in range(1, 8):
            for chars in product('abc', repeat=size):
                text = ''.join(chars)
                strings += 1
                for k in range(1, 10):
                    self.check(text, k)
                    queries += 1
        self.assertEqual((strings, queries), (3279, 29511))

    def test_maximum_length_and_tail_block_thresholds(self):
        text = ''.join(chr(ord('a') + index % 26) for index in range(10000))
        for k in (1, 2, 4999, 5000, 5001, 9999, 10000):
            self.check(text, k)
        self.check('a', 10000, 'a')
        self.check('abcdefg', 2, 'bacdfeg')
        self.check('abcd', 2, 'bacd')
        self.check('abcd', 3, 'cbad')


if __name__ == '__main__':
    unittest.main()
