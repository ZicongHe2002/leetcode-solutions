import unittest
from itertools import product

from python.p0798_smallest_rotation_with_highest_score import Solution


def literal_rotation_scores(values):
    scores = []
    for rotation in range(len(values)):
        rotated = values[rotation:] + values[:rotation]
        scores.append(sum(value <= index for index,value in enumerate(rotated)))
    return scores.index(max(scores))


class BestRotationTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        result = Solution().bestRotation(values)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected)
        self.assertEqual(values,before)

    def test_all_small_legal_arrays_against_actual_rotations(self):
        arrays = 0
        for size in range(1,7):
            for values in product(range(size),repeat=size):
                values = list(values)
                self.check(values,literal_rotation_scores(values))
                arrays += 1
        self.assertEqual(arrays,50069)

    def test_official_examples_ties_and_maximum_size_score_certificates(self):
        self.check([2,3,1,4,0],3)
        self.check([1,3,0,2,4],0)
        self.check([0] * 100000,0)
        self.check([99999] * 100000,0)
        self.check(list(range(100000)),0)
        # For even n, reverse order scores n/2 for even k, n/2+1 for odd k.
        self.check(list(range(99999,-1,-1)),1)


if __name__ == '__main__':
    unittest.main()
