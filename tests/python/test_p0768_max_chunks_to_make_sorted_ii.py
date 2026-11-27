import unittest
from itertools import product

from python.p0768_max_chunks_to_make_sorted_ii import Solution


def all_cut_masks_and_actual_sorted_chunks(values):
    target = sorted(values)
    best = 1
    for mask in range(1 << (len(values) - 1)):
        joined, start, chunks = [], 0, 0
        for end in range(1, len(values) + 1):
            if end == len(values) or mask >> (end - 1) & 1:
                joined.extend(sorted(values[start:end]))
                start, chunks = end, chunks + 1
        if joined == target:
            best = max(best, chunks)
    return best


class MaxChunksTwoTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        result = Solution().maxChunksToSorted(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, all_cut_masks_and_actual_sorted_chunks(values) if expected is None else expected, values[:20])
        self.assertEqual(values, before)

    def test_all_small_duplicate_arrays_against_every_actual_chunk_sorting(self):
        checked = 0
        for size in range(1, 8):
            for values in product(range(3), repeat=size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 3279)

    def test_official_examples_maximum_lengths_duplicates_and_value_bounds(self):
        self.check([5,4,3,2,1], 1)
        self.check([2,1,3,4,4], 4)
        self.check(list(range(2000)), 2000)
        self.check(list(reversed(range(2000))), 1)
        self.check([10**8] * 2000, 2000)
        self.check([10**8,0,10**8], 2)
        self.check([1,1,0,0,1], 2)
        self.check([0], 1)


if __name__ == '__main__':
    unittest.main()
