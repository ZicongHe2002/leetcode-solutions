from itertools import product
import unittest

from python.p0388_longest_absolute_file_path import Solution


def render_and_path_oracle(forest):
    lines, paths = [], []
    def visit(node, ancestors):
        name, children = node
        lines.append('\t' * len(ancestors) + name)
        path = ancestors + [name]
        if children is None:
            paths.append('/'.join(path))
        else:
            for child in children:
                visit(child, path)
    for root in forest:
        visit(root, [])
    return '\n'.join(lines), max(map(len, paths), default=0)


class FilesystemPrefixLengthTests(unittest.TestCase):
    def test_generated_structured_trees_against_materialized_file_paths(self):
        layouts = 0
        for kinds in product(range(3), repeat=5):
            children = []
            for index, kind in enumerate(kinds):
                directory = 'd' * (index + 1)
                file = ('f' * (5 - index) + '.x', None)
                if kind == 0:
                    children.append((directory, []))
                elif kind == 1:
                    children.append(file)
                else:
                    children.append((directory + ' space', [file, ('sub', [])]))
            text, expected = render_and_path_oracle([('root', children)])
            actual = Solution().lengthLongestPath(text)
            self.assertIs(type(actual), int)
            self.assertEqual(actual, expected)
            layouts += 1
        self.assertEqual(layouts, 243)

    def test_multiple_roots_sibling_prefixes_and_maximum_input_length(self):
        for forest in [[('a.x', None)], [('long name', [('f.x', None)]), ('b', [('g.y', None)])],
                       [('dir', [('one', [('file.ext', None)]), ('s', [('x.y', None)])])],
                       [('only', [('directories', [])])]]:
            text, expected = render_and_path_oracle(forest)
            self.assertEqual(Solution().lengthLongestPath(text), expected)
        text = '\n'.join(['\t' * depth + 'a' for depth in range(138)] + ['\t' * 138 + 'f' * 131 + '.x'])
        self.assertEqual(len(text), 10000)
        self.assertEqual(Solution().lengthLongestPath(text), 409)
        self.assertEqual(Solution().lengthLongestPath('a' * 9998 + '.x'), 10000)
        self.assertEqual(Solution().lengthLongestPath(''), 0)


if __name__ == '__main__':
    unittest.main()
