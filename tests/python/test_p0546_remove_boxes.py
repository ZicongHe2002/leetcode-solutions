from functools import lru_cache
from itertools import product
import unittest

from python.p0546_remove_boxes import Solution


@lru_cache(None)
def every_legal_deletion_oracle(state):
    if not state:
        return 0
    answer = 0
    for start in range(len(state)):
        for end in range(start + 1, len(state) + 1):
            if state[end - 1] != state[start]:
                break
            remaining = state[:start] + state[end:]
            answer = max(answer, (end - start) ** 2 + every_legal_deletion_oracle(remaining))
    return answer


class CarriedColorIntervalTests(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def check(self, boxes, expected=None):
        before = boxes[:]
        actual = self.solver.removeBoxes(boxes)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, every_legal_deletion_oracle(tuple(boxes)) if expected is None else expected)
        self.assertEqual(boxes, before)

    def test_all_short_color_sequences_against_every_legal_current_deletion(self):
        arrays = 0
        for size in range(1, 8):
            for boxes in product((1, 2, 3), repeat=size):
                self.check(list(boxes))
                arrays += 1
        self.assertEqual(arrays, 3279)

    def test_maximum_length_color_limits_and_reachable_per_color_square_bounds(self):
        self.check([100] * 100, 10000)
        self.check(list(range(1, 101)), 100)
        self.check([1] * 50 + [100] * 50, 5000)
        self.check([1] * 40 + [100] * 20 + [1] * 40, 6800)
        self.check([1] * 25 + [2] * 25 + [3] * 25 + [1] * 25, 3750)
        self.check([1, 3, 2, 2, 2, 3, 4, 3, 1], 23)
        self.check([1], 1)
        self.check([1, 2, 1, 2, 1, 2])


if __name__ == '__main__':
    unittest.main()
