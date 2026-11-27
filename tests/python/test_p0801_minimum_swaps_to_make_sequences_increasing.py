import unittest
from itertools import product

from python.p0801_minimum_swaps_to_make_sequences_increasing import Solution


def literal_swaps(first, second):
    costs = []
    for mask in range(1 << len(first)):
        left,right = first[:],second[:]
        for index in range(len(first)):
            if mask >> index & 1:
                left[index],right[index] = right[index],left[index]
        if all(left[index - 1] < left[index] and right[index - 1] < right[index]
               for index in range(1,len(first))):
            costs.append(mask.bit_count())
    return min(costs) if costs else None


class MinimumSwapsTests(unittest.TestCase):
    def check(self, first, second, expected):
        before = first[:],second[:]
        result = Solution().minSwap(first,second)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected,(first,second))
        self.assertEqual((first,second),before)

    def test_all_small_candidate_pairs_with_solvable_contract_against_actual_swap_masks(self):
        candidates = solvable = 0
        for size in range(2,5):
            for cells in product(range(4),repeat=2 * size):
                first,second = list(cells[:size]),list(cells[size:])
                expected = literal_swaps(first,second)
                if expected is not None:
                    self.check(first,second,expected)
                    solvable += 1
                candidates += 1
        self.assertEqual(candidates,69888)
        self.assertGreater(solvable,0)

    def test_examples_and_maximum_length_global_orientation_certificates(self):
        self.check([1,3,5,4],[1,2,3,7],1)
        self.check([0,3,5,8,9],[2,1,4,6,9],1)
        self.check(list(range(100000)),list(range(100000)),0)
        first,second = list(range(100000)),list(range(1,100001))
        flipped = 0
        for index in range(0,100000,3):
            first[index],second[index] = second[index],first[index]
            flipped += 1
        self.check(first,second,min(flipped,100000 - flipped))
        self.check([0,200000],[0,200000],0)


if __name__ == '__main__':
    unittest.main()
