from itertools import product
import unittest

from python.p0307_range_sum_query_mutable import NumArray


class MutableFenwickRangeTests(unittest.TestCase):
    def verify_all_ranges(self, instance, values):
        for left in range(len(values)):
            for right in range(left, len(values)):
                result = instance.sumRange(left, right)
                self.assertIs(type(result), int)
                self.assertEqual(result, sum(values[left:right + 1]))

    def test_every_small_initial_array_with_update_and_all_query_sequences(self):
        arrays = 0
        for size in range(1, 6):
            for values in product((-1, 0, 1), repeat=size):
                source, reference = list(values), list(values)
                instance = NumArray(source)
                self.verify_all_ranges(instance, reference)
                for index in range(size):
                    for value in (-2, 0, 2):
                        self.assertIsNone(instance.update(index, value))
                        reference[index] = value
                        self.verify_all_ranges(instance, reference)
                self.assertEqual(source, list(values))
                arrays += 1
        self.assertEqual(arrays, 363)

    def test_maximum_length_combined_call_budget_and_nonzero_initialization(self):
        size = 30000
        source = [0] * size
        reference = source[:]
        instance = NumArray(source)
        for operation in range(15000):
            index = operation * 7919 % size
            value = operation * 37 % 201 - 100
            self.assertIsNone(instance.update(index, value))
            reference[index] = value
            if operation == 14999:
                left, right = 0, size - 1
            elif operation % 2 == 0:
                left = right = index
            else:
                left = index // 1000 * 1000
                right = left + 999
            result = instance.sumRange(left, right)
            self.assertIs(type(result), int)
            self.assertEqual(result, sum(reference[left:right + 1]))
        self.assertEqual(source, [0] * size)
        for value in (-100, 100):
            constant = NumArray([value] * size)
            self.assertEqual(constant.sumRange(0, size - 1), value * size)
            self.assertEqual(constant.sumRange(size - 1, size - 1), value)


if __name__ == '__main__':
    unittest.main()
