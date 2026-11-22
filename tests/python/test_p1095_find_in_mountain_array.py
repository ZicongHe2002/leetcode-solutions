import unittest
from itertools import combinations

from python.p1095_find_in_mountain_array import Solution


class MountainArray:
    __slots__ = ('__values', '__reads')

    def __init__(self, values, reads):
        self.__values = tuple(values)
        self.__reads = reads

    def get(self, index):
        if not 0 <= index < len(self.__values):
            raise AssertionError('get index is outside the mountain')
        self.__reads.append(index)
        if len(self.__reads) > 100:
            raise AssertionError('get call budget exceeded')
        return self.__values[index]

    def length(self):
        return len(self.__values)


def all_small_mountains():
    for peak in range(1, 6):
        slopes = [values for size in range(1, peak + 1)
                  for values in combinations(range(peak), size)]
        for left in slopes:
            for right in slopes:
                yield peak, list(left) + [peak] + list(reversed(right))


class InteractiveMountainSearchTests(unittest.TestCase):
    def check(self, values, target):
        before = values[:]
        expected = next((i for i, value in enumerate(values) if value == target), -1)
        peak = values.index(max(values))
        self.assertTrue(0 < peak < len(values) - 1)
        self.assertTrue(all(values[i] < values[i + 1] for i in range(peak)))
        self.assertTrue(all(values[i] > values[i + 1]
                            for i in range(peak, len(values) - 1)))
        reads = []
        result = Solution().findInMountainArray(target, MountainArray(values, reads))
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertLessEqual(len(reads), 56)
        self.assertEqual(len(reads), len(set(reads)))
        self.assertEqual(values, before)

    def test_all_small_mountains_and_targets_against_first_match(self):
        arrays = checks = 0
        for peak, values in all_small_mountains():
            arrays += 1
            for target in range(peak + 2):
                self.check(values, target)
                checks += 1
        self.assertEqual((arrays, checks), (1245, 8361))

    def test_maximum_length_call_budget_and_minimum_matching_index(self):
        mountains = [
            list(range(5000)) + [10**9] + list(range(4998, -1, -1)),
            [0, 10**9] + list(range(9997, -1, -1)),
            list(range(9999)) + [0],
        ]
        for values in mountains:
            self.assertEqual(len(values), 10000)
            for target in (0, 1, 4998, 4999, 9997, 10**9 - 1, 10**9):
                self.check(values, target)
        self.check([1, 2, 3, 4, 5, 3, 1], 3)
        self.check([0, 1, 2, 4, 2, 1], 3)


if __name__ == '__main__':
    unittest.main()
