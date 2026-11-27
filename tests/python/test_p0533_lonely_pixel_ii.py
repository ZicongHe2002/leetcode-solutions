from itertools import product
import unittest

from python.p0533_lonely_pixel_ii import Solution


def literal_pixel_conditions_oracle(picture, target):
    answer = 0
    for row in range(len(picture)):
        for column in range(len(picture[0])):
            if picture[row][column] != 'B' or picture[row].count('B') != target:
                continue
            black_rows = [other for other in range(len(picture)) if picture[other][column] == 'B']
            if len(black_rows) == target and all(picture[other] == picture[row] for other in black_rows):
                answer += 1
    return answer


class RepeatedRowLonelyPixelTests(unittest.TestCase):
    def check(self, picture, target, expected=None):
        before = [row[:] for row in picture]
        identities = tuple(map(id, picture))
        actual = Solution().findBlackPixel(picture, target)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, literal_pixel_conditions_oracle(picture, target) if expected is None else expected)
        self.assertEqual(picture, before)
        self.assertEqual(tuple(map(id, picture)), identities)

    def test_all_small_pictures_and_targets_against_literal_pixel_rules(self):
        pictures = queries = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for pixels in product('BW', repeat=rows * columns):
                    picture = [list(pixels[start:start + columns]) for start in range(0, len(pixels), columns)]
                    pictures += 1
                    for target in range(1, min(rows, columns) + 1):
                        self.check(picture, target)
                        queries += 1
        self.assertEqual((pictures, queries), (682, 1850))

    def test_maximum_dimensions_duplicate_frequency_and_nonidentical_rows(self):
        self.check([['B'] * 200 for _ in range(200)], 200, 40000)
        self.check([['B'] * 200 for _ in range(200)], 199, 0)
        self.check([['B' if row == column else 'W' for column in range(200)] for row in range(200)], 1, 200)
        picture = [['B'] * 100 + ['W'] * 100 for _ in range(100)] + [['W'] * 200 for _ in range(100)]
        self.check(picture, 100, 10000)
        self.check([list('BWB'), list('BBW')], 2, 0)
        self.check([list('WBWBBW')] * 3 + [list('WWBWBW')], 3, 6)
        self.check([['B']], 1, 1)
        self.check([['W']], 1, 0)


if __name__ == '__main__':
    unittest.main()
