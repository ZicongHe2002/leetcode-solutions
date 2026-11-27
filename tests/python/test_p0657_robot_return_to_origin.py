import unittest
from itertools import product

from python.p0657_robot_return_to_origin import Solution


def walk(moves):
    x = y = 0
    for move in moves:
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y += 1
        else:
            y -= 1
    return x == y == 0


class RobotOriginTests(unittest.TestCase):
    def check(self, moves, expected=None):
        if expected is None:
            expected = walk(moves)
        actual = Solution().judgeCircle(moves)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected)

    def test_every_short_direction_string_against_actual_walk(self):
        checked = 0
        for length in range(1, 9):
            for moves in product('LRUD', repeat=length):
                self.check(''.join(moves))
                checked += 1
        self.assertEqual(checked, 87380)

    def test_maximum_length_one_axis_imbalance_and_final_position(self):
        self.check('U' * 10000 + 'D' * 10000, True)
        self.check('LR' * 10000, True)
        self.check('UD' * 9999 + 'UU', False)
        self.check('L' * 20000, False)
        self.check('UD' + 'R' * 19998, False)
        self.check('UDR', False)


if __name__ == '__main__':
    unittest.main()
