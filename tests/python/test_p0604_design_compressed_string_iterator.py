from itertools import product
import re
import unittest

from python.p0604_design_compressed_string_iterator import StringIterator


def expand_small(compressed):
    return ''.join(letter * int(count) for letter, count in re.findall(r'([A-Za-z])(\d+)', compressed))


class CompressedIteratorTests(unittest.TestCase):
    def check_small(self, compressed):
        expected = expand_small(compressed)
        iterator = StringIterator(compressed)
        calls = 0
        for letter in expected:
            for _ in range(2):
                result = iterator.hasNext()
                self.assertIs(type(result), bool)
                self.assertTrue(result)
                calls += 1
            result = iterator.next()
            self.assertIs(type(result), str)
            self.assertEqual(result, letter)
            calls += 1
        self.assertFalse(iterator.hasNext())
        self.assertEqual(iterator.next(), ' ')
        self.assertEqual(iterator.next(), ' ')
        self.assertFalse(iterator.hasNext())
        calls += 4
        self.assertLessEqual(calls, 100)

    def test_all_small_run_sequences_against_expansion_and_nonconsuming_queries(self):
        runs = [letter + str(count) for letter in ('A', 'b') for count in range(1, 4)]
        cases = 0
        for size in range(1, 5):
            for sequence in product(runs, repeat=size):
                self.check_small(''.join(sequence))
                cases += 1
        self.assertEqual(cases, 1554)

    def test_multi_digit_runs_billion_count_and_maximum_encoded_length(self):
        for compressed in ('X12Y2', 'a10b1a10', 'x11X12y1', 'a1a1B1'):
            self.check_small(compressed)
        huge = StringIterator('Z1000000000a1')
        for call in range(100):
            if call % 10 == 0:
                self.assertIs(huge.hasNext(), True)
            else:
                self.assertEqual(huge.next(), 'Z')
        compressed = 'A1b1' * 250
        self.assertEqual(len(compressed), 1000)
        long_iterator = StringIterator(compressed)
        expanded = 'Ab' * 250
        cursor = 0
        for call in range(100):
            if call % 2 == 0:
                self.assertIs(long_iterator.hasNext(), True)
            else:
                self.assertEqual(long_iterator.next(), expanded[cursor])
                cursor += 1


if __name__ == '__main__':
    unittest.main()
