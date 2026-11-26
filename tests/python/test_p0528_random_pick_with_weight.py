from collections import Counter
from itertools import product
from unittest.mock import patch
import unittest

from python.p0528_random_pick_with_weight import Solution


def explicit_slot_owners(weights):
    return [index for index, weight in enumerate(weights) for _ in range(weight)]


class IntegerWeightSlotTests(unittest.TestCase):
    def test_every_slot_of_all_short_weight_arrays_against_explicit_owners(self):
        arrays = calls = 0
        for size in range(1, 6):
            for values in product((1, 2, 3), repeat=size):
                weights = list(values)
                before = weights[:]
                expected = explicit_slot_owners(weights)
                sampler = Solution(weights)
                with patch('python.p0528_random_pick_with_weight.randrange',
                           side_effect=range(len(expected))) as draw:
                    actual = [sampler.pickIndex() for _ in expected]
                self.assertEqual(actual, expected)
                self.assertTrue(all(type(index) is int for index in actual))
                self.assertEqual(Counter(actual), dict(enumerate(weights)))
                self.assertEqual(weights, before)
                self.assertEqual(draw.call_count, len(expected))
                self.assertTrue(all(call.args == (len(expected),) for call in draw.call_args_list))
                arrays += 1
                calls += len(expected)
        self.assertEqual((arrays, calls), (363, 3282))

    def test_maximum_length_weight_call_count_and_exact_cumulative_boundaries(self):
        weights = [100000] * 10000
        before = weights[:]
        sampler = Solution(weights)
        slots = [index * 100000 + 99999 for index in range(10000)]
        with patch('python.p0528_random_pick_with_weight.randrange', side_effect=slots) as draw:
            self.assertEqual([sampler.pickIndex() for _ in slots], list(range(10000)))
        self.assertEqual(draw.call_count, 10000)
        self.assertTrue(all(call.args == (10**9,) for call in draw.call_args_list))
        self.assertEqual(weights, before)
        sampler = Solution([1, 100000, 1])
        with patch('python.p0528_random_pick_with_weight.randrange', side_effect=[0, 1, 100000, 100001]):
            self.assertEqual([sampler.pickIndex() for _ in range(4)], [0, 1, 1, 2])
        sampler = Solution([100000])
        with patch('python.p0528_random_pick_with_weight.randrange', side_effect=[0, 99999]):
            self.assertEqual([sampler.pickIndex(), sampler.pickIndex()], [0, 0])


if __name__ == '__main__':
    unittest.main()
