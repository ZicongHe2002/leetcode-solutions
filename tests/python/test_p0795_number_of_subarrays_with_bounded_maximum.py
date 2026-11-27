import unittest
from itertools import product

from python.p0795_number_of_subarrays_with_bounded_maximum import Solution


def literal_intervals(values, lower, upper):
    return sum(lower <= max(values[start:end]) <= upper
               for start in range(len(values)) for end in range(start + 1,len(values) + 1))


class BoundedMaximumTests(unittest.TestCase):
    def check(self, values, lower, upper, expected):
        before = values[:]
        result = Solution().numSubarrayBoundedMax(values,lower,upper)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected)
        self.assertLessEqual(result,2**31 - 1)
        self.assertEqual(values,before)

    def test_all_small_arrays_and_closed_bounds_against_literal_slice_maxima(self):
        arrays = queries = 0
        for size in range(1,7):
            for values in product(range(4),repeat=size):
                values = list(values)
                arrays += 1
                for lower in range(4):
                    for upper in range(lower,4):
                        self.check(values,lower,upper,literal_intervals(values,lower,upper))
                        queries += 1
        self.assertEqual((arrays,queries),(5460,54600))

    def test_examples_size_value_and_legal_answer_limits(self):
        self.check([2,1,4,3],2,3,3)
        self.check([2,9,2,5,6],2,8,7)
        self.check([0,10**9] * 50000,0,0,50000)
        self.check([1] * 100000,2,2,0)
        self.check([10**9] * 65535,10**9,10**9,2147450880)
        self.check([0],0,0,1)


if __name__ == '__main__':
    unittest.main()
