import string
import unittest
from itertools import product

from python.p0806_number_of_lines_to_write_string import Solution


def all_line_partitions(widths, text):
    pixels = [widths[ord(char) - ord('a')] for char in text]
    best_ends = None
    best_widths = None
    for mask in range(1 << (len(text) - 1)):
        ends = [index + 1 for index in range(len(text) - 1) if mask >> index & 1] + [len(text)]
        starts = [0] + ends[:-1]
        amounts = [sum(pixels[start:end]) for start,end in zip(starts,ends)]
        if all(amount <= 100 for amount in amounts) and (best_ends is None or ends > best_ends):
            best_ends,best_widths = ends,amounts
    return [len(best_ends),best_widths[-1]]


class NumberOfLinesTests(unittest.TestCase):
    def check(self, widths, text, expected):
        before = widths[:]
        result = Solution().numberOfLines(widths,text)
        self.assertIs(type(result),list)
        self.assertEqual(result,expected)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(widths,before)

    def test_small_boundary_texts_against_every_possible_line_partition(self):
        checked = 0
        for first,second in product((2,7,10),repeat=2):
            widths = [first,second] + [5] * 24
            for size in range(4):
                for chars in product('ab',repeat=size):
                    text = 'a' * 10 + ''.join(chars)
                    self.check(widths,text,all_line_partitions(widths,text))
                    checked += 1
        self.assertEqual(checked,135)

    def test_examples_all_letter_indices_and_maximum_length_constant_width_certificates(self):
        self.check([10] * 26,string.ascii_lowercase,[3,60])
        self.check([4] + [10] * 25,'bbbcccdddaaa',[2,4])
        self.check([10] * 26,'a' * 10,[1,100])
        self.check([10] * 26,'a' * 11,[2,10])
        widths = [2 + index % 9 for index in range(26)]
        for index,char in enumerate(string.ascii_lowercase):
            width = widths[index]
            capacity = 100 // width
            self.check(widths,char * 1000,[(999 // capacity) + 1,(999 % capacity + 1) * width])
        self.check([2] * 26,'z',[1,2])


if __name__ == '__main__':
    unittest.main()
