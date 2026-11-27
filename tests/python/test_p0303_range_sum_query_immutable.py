from itertools import product
import unittest

from python.p0303_range_sum_query_immutable import NumArray


class ImmutablePrefixRangeTests(unittest.TestCase):
    def test_every_small_array_and_every_inclusive_interval(self):
        arrays = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                source = list(values)
                before = source[:]
                instance = NumArray(source)
                for left in range(size):
                    for right in range(left, size):
                        result = instance.sumRange(left, right)
                        self.assertIs(type(result), int)
                        self.assertEqual(result, sum(before[left:right + 1]))
                self.assertEqual(source, before)
                arrays += 1
        self.assertEqual(arrays, 3279)

    def test_maximum_length_and_query_count_signed_value_extremes(self):
        size = 10000
        source = [-100000, 100000] * 5000
        before = source[:]
        instance = NumArray(source)
        for query in range(10000):
            if query == 0:
                left, right = 0, size - 1
            elif query == 1:
                left = right = 0
            elif query == 2:
                left = right = size - 1
            else:
                left = query * 37 % size
                right = left + query * 97 % (size - left)
            expected = 0 if (right - left + 1) % 2 == 0 else before[left]
            result = instance.sumRange(left, right)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)
        self.assertEqual(source, before)
        for value in (-100000, 100000):
            constant = NumArray([value] * size)
            self.assertEqual(constant.sumRange(0, size - 1), value * size)
            self.assertEqual(constant.sumRange(size - 1, size - 1), value)


if __name__ == '__main__':
    unittest.main()
