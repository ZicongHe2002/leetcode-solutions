import unittest
from itertools import product

from python.p0347_top_k_frequent_elements import Solution


class SolutionTests(unittest.TestCase):
    def check(self, values, expected, *args):
        before = values[:]
        actual = Solution().topKFrequent(values, *args)
        self.assertEqual(sorted(actual), expected)
        self.assertEqual(values, before)

    def test_small_arrays_and_every_unique_answer_k(self):
        checked = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                ranked = sorted(set(values), key=lambda value: (-values.count(value), value))
                for k in range(1, len(ranked) + 1):
                    if k < len(ranked) and values.count(ranked[k - 1]) == values.count(ranked[k]):
                        continue
                    self.check(list(values), sorted(ranked[:k]), k)
                    checked += 1
        self.assertGreater(checked, 3279)

    def test_maximum_length_and_all_distinct_values(self):
        self.check([1] * 50000 + [2] * 30000 + [3] * 20000, [1, 2], 2)
        self.check([0] * 100000, [0], 1)
        values = list(range(-5000, 5000))
        self.check(values, values[:], len(values))

if __name__ == '__main__':
    unittest.main()
