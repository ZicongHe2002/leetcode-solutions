from itertools import product
import unittest

from python.p0454_4sum_ii import Solution


def every_four_indices_oracle(arrays):
    return sum(first + second + third + fourth == 0 for first, second, third, fourth in product(*arrays))


class FourArrayIndexMultiplicityTests(unittest.TestCase):
    def check(self, arrays, expected=None):
        before = [values[:] for values in arrays]
        actual = Solution().fourSumCount(*arrays)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, every_four_indices_oracle(arrays) if expected is None else expected)
        self.assertEqual(arrays, before)

    def test_every_small_equal_length_four_array_combination(self):
        groups = 0
        for size in range(3):
            choices = tuple(product((-1, 0, 1), repeat=size))
            for arrays in product(choices, repeat=4):
                self.check([list(values) for values in arrays])
                groups += 1
        self.assertEqual(groups, 6643)

    def test_maximum_length_multiplicity_integer_bounds_and_no_solution(self):
        self.check([[0] * 200 for _ in range(4)], 200**4)
        self.check([[-2**28] * 200, [2**28 - 1] * 200, [1] * 200, [0] * 200], 200**4)
        self.check([[2**28], [-2**28], [0], [0]], 1)
        self.check([[1] * 200 for _ in range(4)], 0)
        self.check([[1, 2], [-2, -1], [-1, 2], [0, 2]], 2)


if __name__ == '__main__':
    unittest.main()
