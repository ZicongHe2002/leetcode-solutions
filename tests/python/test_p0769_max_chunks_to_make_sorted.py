import unittest
from itertools import permutations

from python.p0769_max_chunks_to_make_sorted import Solution


def actual_sorting_of_every_cut_pattern(values):
    expected = sorted(values)
    best = 1
    for mask in range(1 << (len(values) - 1)):
        output, begin, count = [], 0, 0
        for end in range(1, len(values) + 1):
            if end == len(values) or mask >> (end - 1) & 1:
                output.extend(sorted(values[begin:end]))
                begin, count = end, count + 1
        if output == expected:
            best = max(best, count)
    return best


class MaxChunksOneTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        result = Solution().maxChunksToSorted(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, actual_sorting_of_every_cut_pattern(values) if expected is None else expected, values)
        self.assertEqual(values, before)

    def test_every_small_permutation_against_all_actual_sorted_chunk_concatenations(self):
        checked = 0
        for size in range(1, 8):
            for values in permutations(range(size)):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 5913)

    def test_official_examples_maximum_permutations_and_prefix_not_current_value(self):
        self.check([4,3,2,1,0], 1)
        self.check([1,0,2,3,4], 4)
        self.check(list(range(10)), 10)
        self.check(list(reversed(range(10))), 1)
        self.check([2,1,0,3], 2)
        self.check([0], 1)


if __name__ == '__main__':
    unittest.main()
