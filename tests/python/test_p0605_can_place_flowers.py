from itertools import product
import unittest

from python.p0605_can_place_flowers import Solution


def all_added_subsets(values):
    empty = [index for index, value in enumerate(values) if value == 0]
    best = 0
    for mask in range(1 << len(empty)):
        candidate = values[:]
        for bit, index in enumerate(empty):
            if mask >> bit & 1:
                candidate[index] = 1
        if not any(left and right for left, right in zip(candidate, candidate[1:])):
            best = max(best, mask.bit_count())
    return best


class VirtualFlowerPlantingTests(unittest.TestCase):
    def check(self, values, needed, expected):
        before = values[:]
        result = Solution().canPlaceFlowers(values, needed)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_legal_beds_and_requests_against_new_subsets(self):
        beds = checks = 0
        for size in range(1, 10):
            for values in product((0, 1), repeat=size):
                if any(left and right for left, right in zip(values, values[1:])):
                    continue
                beds += 1
                values = list(values)
                capacity = all_added_subsets(values)
                for needed in range(size + 1):
                    self.check(values, needed, capacity >= needed)
                    checks += 1
        self.assertEqual((beds, checks), (230, 1955))

    def test_maximum_length_exact_capacity_and_existing_flowers(self):
        self.check([0] * 20000, 10000, True)
        self.check([0] * 20000, 10001, False)
        self.check([0] * 19999, 10000, True)
        self.check([1, 0] * 10000, 1, False)
        self.check([1, 0] * 10000, 0, True)
        self.check([0], 1, True)
        self.check([1], 1, False)


if __name__ == '__main__':
    unittest.main()
