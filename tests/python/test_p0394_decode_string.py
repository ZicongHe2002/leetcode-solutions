import unittest
from itertools import product

from python.p0394_decode_string import Solution


def render_tree(node):
    if isinstance(node, str):
        return node
    count, children = node
    return str(count) + '[' + ''.join(render_tree(child) for child in children) + ']'


def expand_tree(node):
    if isinstance(node, str):
        return node
    count, children = node
    return ''.join(expand_tree(child) for child in children) * count


class DecodeStringTests(unittest.TestCase):
    def check(self, encoded, expected):
        result = Solution().decodeString(encoded)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)

    def test_generated_nested_trees_against_direct_tree_expansion(self):
        checks = 0
        choices = product(('', 'a', 'b', 'ab'), ('a', 'b', 'ab'), range(1, 4), range(1, 4), ('', 'a', 'ba'))
        for prefix, middle, inner, outer, suffix in choices:
            nodes = (prefix, (outer, (middle, (inner, (middle[::-1],)))), suffix)
            self.check(''.join(render_tree(node) for node in nodes), ''.join(expand_tree(node) for node in nodes))
            checks += 1
        self.assertEqual(checks, 324)

    def test_output_limit_repeat_limit_multiple_digits_and_adjacent_frames(self):
        self.check('100[100[10[a]]]', 'a' * 100000)
        self.check('300[ab]', 'ab' * 300)
        self.check('1[' * 9 + 'a' + ']' * 9, 'a')
        self.check('10[a]2[bc]', 'a' * 10 + 'bcbc')
        self.check('2[ab]3[c]', 'ababccc')
        self.check('abcdefghijklmnopqrstuvwxyzabcd', 'abcdefghijklmnopqrstuvwxyzabcd')


if __name__ == '__main__':
    unittest.main()
