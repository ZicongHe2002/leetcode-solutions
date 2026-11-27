from itertools import product
from math import factorial
from random import Random
from unittest.mock import patch
import unittest

import python.p0519_random_flip_matrix as module


class SparseFlipPermutationTests(unittest.TestCase):
    def test_all_rank_draw_branches_are_a_bijection_to_cell_permutations(self):
        branches = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 2), (2, 3), (3, 2)):
            size = rows * columns
            orders = set()
            for ranks in product(*(range(bound) for bound in range(size, 0, -1))):
                sampler = module.Solution(rows, columns)
                chosen_ranks = iter(ranks)
                bounds = []

                def draw(bound):
                    bounds.append(bound)
                    return next(chosen_ranks)

                cells = []
                with patch.object(module, 'randrange', draw):
                    for _ in range(size):
                        cell = sampler.flip()
                        self.assertIs(type(cell), list)
                        self.assertEqual(len(cell), 2)
                        row, column = cell
                        self.assertTrue(type(row) is int and type(column) is int)
                        self.assertTrue(0 <= row < rows and 0 <= column < columns)
                        cells.append((row, column))
                self.assertEqual(bounds, list(range(size, 0, -1)))
                self.assertEqual(len(set(cells)), size)
                orders.add(tuple(cells))
                branches += 1
            self.assertEqual(len(orders), factorial(size))
        self.assertEqual(branches, 1481)

    def test_reset_epochs_and_maximum_matrix_with_exact_call_limit(self):
        generator = Random(519)
        with patch.object(module, 'randrange', generator.randrange):
            sampler = module.Solution(2, 3)
            expected = {(row, column) for row in range(2) for column in range(3)}
            for _ in range(10):
                self.assertEqual({tuple(sampler.flip()) for _ in range(6)}, expected)
                self.assertIsNone(sampler.reset())
            sampler = module.Solution(10000, 10000)
            cells = [tuple(sampler.flip()) for _ in range(998)]
            self.assertEqual(len(set(cells)), 998)
            self.assertTrue(all(0 <= row < 10000 and 0 <= column < 10000 for row, column in cells))
            self.assertLessEqual(len(sampler.remap), 998)
            self.assertIsNone(sampler.reset())
            self.assertEqual(sampler.remap, {})
            self.assertEqual(sampler.remaining, 100000000)
            row, column = sampler.flip()
            self.assertTrue(0 <= row < 10000 and 0 <= column < 10000)


if __name__ == '__main__':
    unittest.main()
