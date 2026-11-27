import unittest
from itertools import product

from python.p0703_kth_largest_element_in_a_stream import KthLargest


class KthLargestStreamTests(unittest.TestCase):
    def check(self, initial, k, additions):
        before, history = initial[:], initial[:]
        obj = KthLargest(k, initial)
        checked = 0
        for value in additions:
            history.append(value)
            result = obj.add(value)
            self.assertIs(type(result), int)
            self.assertEqual(result, sorted(history, reverse=True)[k - 1])
            self.assertEqual(initial, before)
            checked += 1
        return checked

    def test_all_small_initial_arrays_k_and_add_programs_against_full_history_sort(self):
        instances = checked = 0
        additions = [values for size in range(1, 4) for values in product((-1, 0, 1), repeat=size)]
        for size in range(4):
            for initial in product((-1, 0, 1), repeat=size):
                for k in range(1, size + 2):
                    for program in additions:
                        checked += self.check(list(initial), k, program)
                        instances += 1
        self.assertEqual((instances, checked), (5538, 14484))

    def test_ten_thousand_initial_scores_adds_duplicates_and_boundary_k(self):
        initial = list(range(-10000, 0))
        before = initial[:]
        obj = KthLargest(10000, initial)
        for count, value in enumerate(range(10000), 1):
            result = obj.add(value)
            self.assertIs(type(result), int)
            self.assertEqual(result, count - 10000)
        self.assertEqual(initial, before)
        self.check(initial, 10001, [10000, -10000])
        self.check([], 1, [-10000, 10000, 0])
        self.check([4, 5, 8, 2], 3, [3, 5, 10, 9, 4])
        self.check([7, 7, 7, 7, 8, 3], 4, [2, 10, 9, 9])


if __name__ == '__main__':
    unittest.main()
