from itertools import product
import unittest

from python.p0436_find_right_interval import Solution


def linear_candidate_oracle(intervals):
    result = []
    for _, end in intervals:
        candidates = [(start, index) for index, (start, _) in enumerate(intervals) if start >= end]
        result.append(min(candidates)[1] if candidates else -1)
    return result


class RightIntervalOriginalIndexTests(unittest.TestCase):
    def check(self, intervals, expected=None):
        before = [item[:] for item in intervals]
        identities = [id(item) for item in intervals]
        actual = Solution().findRightInterval(intervals)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, linear_candidate_oracle(intervals) if expected is None else expected)
        self.assertEqual(intervals, before)
        self.assertEqual([id(item) for item in intervals], identities)

    def test_all_small_unique_start_layouts_in_both_input_orders(self):
        starts = tuple(range(-2, 3))
        options = [(None, *range(start, 4)) for start in starts]
        layouts = queries = 0
        for ends in product(*options):
            intervals = [[start, end] for start, end in zip(starts, ends) if end is not None]
            self.check(intervals)
            self.check(list(reversed(intervals)))
            layouts += 1
            queries += 2
        self.assertEqual((layouts, queries), (2520, 5040))

    def test_maximum_count_equal_endpoint_and_coordinate_bounds(self):
        self.check([[index, index + 1] for index in range(20000)], list(range(1, 20000)) + [-1])
        self.check([[index, index] for index in range(20000)], list(range(20000)))
        self.check([[-10**6, -10**6], [10**6, 10**6]], [0, 1])
        self.check([[1, 2]], [-1])
        self.check([[1, 1]], [0])


if __name__ == '__main__':
    unittest.main()
