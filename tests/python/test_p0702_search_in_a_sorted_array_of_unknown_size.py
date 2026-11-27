import unittest
from itertools import combinations

from python.p0702_search_in_a_sorted_array_of_unknown_size import Solution


class Reader:
    __slots__ = ('__values', 'calls')

    def __init__(self, values):
        self.__values = tuple(values)
        self.calls = []

    def get(self, index):
        if type(index) is not int or index < 0:
            raise AssertionError('get requires a nonnegative integer index')
        self.calls.append(index)
        return self.__values[index] if index < len(self.__values) else 2**31 - 1


class UnknownSizeSearchTests(unittest.TestCase):
    def check(self, values, target):
        before = values[:]
        reader = Reader(values)
        result = Solution().search(reader, target)
        self.assertIs(type(result), int)
        expected = values.index(target) if target in values else -1
        self.assertEqual(result, expected, (values[:10], target))
        self.assertLessEqual(len(reader.calls), 2 * (len(values) + 1).bit_length() + 4)
        self.assertEqual(values, before)

    def test_all_small_sorted_subsets_and_targets_against_direct_index_oracle(self):
        arrays = checked = 0
        pool = (-4, -2, -1, 0, 2, 5, 8)
        for size in range(1, len(pool) + 1):
            for values in combinations(pool, size):
                arrays += 1
                for target in range(-5, 10):
                    self.check(list(values), target)
                    checked += 1
        self.assertEqual((arrays, checked), (127, 1905))

    def test_ten_thousand_elements_sentinel_expansion_and_singleton_boundaries(self):
        values = list(range(-10000, 10000, 2))
        self.assertEqual(len(values), 10000)
        for target in (-10000, -9999, -5000, 0, 9998, 9999, 10000):
            self.check(values, target)
        for values in ([-10000], [10000]):
            for target in (-10000, 0, 10000):
                self.check(values, target)
        self.check([-1, 0, 3, 5, 9, 12], 9)
        self.check([-1, 0, 3, 5, 9, 12], 2)


if __name__ == '__main__':
    unittest.main()
