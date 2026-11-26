from itertools import product
import unittest

from python.p0335_self_crossing import Solution


def orientation(first, second, third):
    return (second[0] - first[0]) * (third[1] - first[1]) - (second[1] - first[1]) * (third[0] - first[0])


def on_segment(first, second, point):
    return min(first[0], second[0]) <= point[0] <= max(first[0], second[0]) and min(first[1], second[1]) <= point[1] <= max(first[1], second[1])


def intersects(first, second, third, fourth):
    a, b = orientation(first, second, third), orientation(first, second, fourth)
    c, d = orientation(third, fourth, first), orientation(third, fourth, second)
    if a == 0 and on_segment(first, second, third):
        return True
    if b == 0 and on_segment(first, second, fourth):
        return True
    if c == 0 and on_segment(third, fourth, first):
        return True
    if d == 0 and on_segment(third, fourth, second):
        return True
    return a * b < 0 and c * d < 0


def all_segments_oracle(distances):
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
    position = (0, 0)
    segments = []
    for index, length in enumerate(distances):
        dx, dy = directions[index % 4]
        following = (position[0] + dx * length, position[1] + dy * length)
        for first, second in segments[:-1]:
            if intersects(first, second, position, following):
                return True
        segments.append((position, following))
        position = following
    return False


class LocalCrossingGeometryTests(unittest.TestCase):
    def check(self, distances, expected=None):
        before = distances[:]
        expected = all_segments_oracle(distances) if expected is None else expected
        actual = Solution().isSelfCrossing(distances)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected)
        self.assertEqual(distances, before)

    def test_all_small_positive_paths_against_explicit_segment_geometry(self):
        arrays = 0
        for size in range(1, 10):
            for values in product((1, 2, 3), repeat=size):
                self.check(list(values))
                arrays += 1
        self.assertEqual(arrays, 29523)

    def test_three_local_cases_contact_and_maximum_path_length(self):
        self.check([2, 1, 1, 2], True)
        self.check([1, 1, 2, 1, 1], True)
        self.check([1, 1, 2, 2, 1, 1], True)
        self.check([1, 2, 3, 4], False)
        self.check(list(range(1, 100001)), False)
        self.check(list(range(100000, 0, -1)), False)
        self.check([1] * 100000, True)


if __name__ == '__main__':
    unittest.main()
