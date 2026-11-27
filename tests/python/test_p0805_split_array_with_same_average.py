import random
import unittest
from itertools import combinations, product

from python.p0805_split_array_with_same_average import Solution


def literal_original_average_partitions(values):
    total = sum(values)
    size = len(values)
    for chosen_size in range(1,size):
        for indices in combinations(range(size),chosen_size):
            selected = sum(values[index] for index in indices)
            if selected * (size - chosen_size) == (total - selected) * chosen_size:
                return True
    return False


class SameAverageTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        result = Solution().splitArraySameAverage(values)
        self.assertIs(type(result),bool)
        self.assertEqual(result,expected,values)
        self.assertEqual(values,before)

    def test_all_small_arrays_and_seeded_inputs_against_original_subset_averages(self):
        checked = 0
        for size in range(1,7):
            for values in product(range(4),repeat=size):
                values = list(values)
                self.check(values,literal_original_average_partitions(values))
                checked += 1
        self.assertEqual(checked,5460)
        generator = random.Random(805)
        for _ in range(200):
            values = [generator.randrange(10001) for _ in range(generator.randrange(1,13))]
            self.check(values,literal_original_average_partitions(values))

    def test_examples_nonempty_proper_subset_and_maximum_bounds(self):
        self.check([1,2,3,4,5,6,7,8],True)
        self.check([3,1],False)
        self.check([0],False)
        self.check([0,0],True)
        self.check([10000] * 30,True)
        self.check([0] * 29 + [30],False)
        self.check([1] * 29 + [2],False)
        self.check([0,10000] * 15,True)


if __name__ == '__main__':
    unittest.main()
