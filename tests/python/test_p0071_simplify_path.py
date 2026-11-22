import posixpath
import unittest
from itertools import product

from python.p0071_simplify_path import Solution


def standard_unix_normalization(path):
    return '/' + posixpath.normpath(path).lstrip('/')


class AbsolutePathTests(unittest.TestCase):
    def check(self, path, expected=None):
        if expected is None:
            expected = standard_unix_normalization(path)
        result = Solution().simplifyPath(path)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)

    def test_component_sequences_against_posix_normalization(self):
        checks = 0
        for size in range(7):
            for components in product(('', '.', '..', 'a', '...', 'b_c'), repeat=size):
                self.check('/' + '/'.join(components))
                checks += 1
        self.assertEqual(checks, 55987)

    def test_length_limit_root_parents_normal_names_and_double_slashes(self):
        path = '/' + 'a/' * 1499 + 'a'
        self.assertEqual(len(path), 3000)
        self.check(path, path)
        self.check('/' + '../' * 999, '/')
        self.check('/' + 'x' * 2999, '/' + 'x' * 2999)
        self.check('/.../a.././../b/', '/.../b')
        self.check('//home//foo/', '/home/foo')
        self.check('/a/../../b/../c//.//', '/c')


if __name__ == '__main__':
    unittest.main()
