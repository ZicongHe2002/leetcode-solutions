from itertools import product
import unittest

from python.p0661_image_smoother import Solution


def integral_image_reference(image):
    rows, columns = len(image), len(image[0])
    prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
    for row in range(rows):
        running = 0
        for column in range(columns):
            running += image[row][column]
            prefix[row + 1][column + 1] = prefix[row][column + 1] + running
    output = []
    for row in range(rows):
        top, bottom = max(0, row - 1), min(rows, row + 2)
        output_row = []
        for column in range(columns):
            left, right = max(0, column - 1), min(columns, column + 2)
            total = prefix[bottom][right] - prefix[top][right] - prefix[bottom][left] + prefix[top][left]
            output_row.append(total // ((bottom - top) * (right - left)))
        output.append(output_row)
    return output


class ClippedNeighborhoodSmootherTests(unittest.TestCase):
    def check(self, image, expected=None):
        before = [row[:] for row in image]
        if expected is None:
            expected = integral_image_reference(image)
        result = Solution().imageSmoother(image)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(row) is list for row in result))
        self.assertEqual(result, expected)
        self.assertEqual(image, before)

    def test_all_small_three_graylevel_matrices_against_integral_image(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for flat in product((0, 1, 255), repeat=rows * columns):
                    self.check([list(flat[start:start + columns])
                                for start in range(0, len(flat), columns)])
                    checks += 1
        self.assertEqual(checks, 21297)

    def test_maximum_image_degenerate_axes_and_noninteger_averages(self):
        self.check([[0] * 200 for _ in range(200)])
        self.check([[255] * 200 for _ in range(200)])
        self.check([[255 * ((row + column) % 2) for column in range(200)] for row in range(200)])
        self.check([list(range(200))])
        self.check([[value] for value in range(200)])
        self.check([[100, 200, 100], [200, 50, 200], [100, 200, 100]],
                   [[137, 141, 137], [141, 138, 141], [137, 141, 137]])


if __name__ == '__main__':
    unittest.main()
