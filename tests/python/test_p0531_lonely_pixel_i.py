from itertools import product
import unittest

from python.p0531_lonely_pixel_i import Solution


def inspect_other_pixels_oracle(picture):
    answer = 0
    for row in range(len(picture)):
        for column in range(len(picture[0])):
            if picture[row][column] != 'B':
                continue
            if any(picture[row][other] == 'B' for other in range(len(picture[0])) if other != column):
                continue
            if any(picture[other][column] == 'B' for other in range(len(picture)) if other != row):
                continue
            answer += 1
    return answer


class LonelyBlackPixelTests(unittest.TestCase):
    def check(self, picture, expected=None):
        before = [row[:] for row in picture]
        identities = tuple(map(id, picture))
        actual = Solution().findLonelyPixel(picture)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, inspect_other_pixels_oracle(picture) if expected is None else expected)
        self.assertEqual(picture, before)
        self.assertEqual(tuple(map(id, picture)), identities)

    def test_all_small_black_white_matrices_against_direct_row_column_inspection(self):
        count = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for pixels in product('BW', repeat=rows * columns):
                    picture = [list(pixels[start:start + columns]) for start in range(0, len(pixels), columns)]
                    self.check(picture)
                    count += 1
        self.assertEqual(count, 682)

    def test_maximum_dimensions_diagonal_uniform_and_single_dimension(self):
        self.check([['B' if row == column else 'W' for column in range(500)] for row in range(500)], 500)
        self.check([['B'] * 500 for _ in range(500)], 0)
        self.check([['W'] * 500 for _ in range(500)], 0)
        self.check([['W'] * 499 + ['B']], 1)
        self.check([['B'] * 500], 0)
        self.check([['W'] for _ in range(499)] + [['B']], 1)
        self.check([['B'] for _ in range(500)], 0)
        self.check([['B']], 1)
        self.check([['W']], 0)


if __name__ == '__main__':
    unittest.main()
