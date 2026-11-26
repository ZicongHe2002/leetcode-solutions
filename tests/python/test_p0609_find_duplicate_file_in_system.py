from itertools import product
import unittest

from python.p0609_find_duplicate_file_in_system import Solution


def pairwise_content_groups(records):
    seen, groups = set(), []
    for path, content in records:
        if path in seen:
            continue
        group = [other_path for other_path, other_content in records if other_content == content]
        seen.update(group)
        if len(group) > 1:
            groups.append(group)
    return groups


def fixture(contents, layout):
    directories, records = {}, []
    for index, content in enumerate(contents):
        if layout == 0:
            directory, name = 'root', f'f{index}.txt'
        elif layout == 1:
            directory, name = f'root/d{index}', 'same.txt'
        else:
            directory = 'root/a' if index % 2 == 0 else 'root/b'
            name = f'f{index // 2}.txt'
        directories.setdefault(directory, []).append(name + '(' + content + ')')
        records.append((directory + '/' + name, content))
    paths = [directory + ' ' + ' '.join(entries) for directory, entries in directories.items()]
    return paths, records


def normalized(groups):
    return {frozenset(group) for group in groups}


class DuplicateFileTests(unittest.TestCase):
    def check(self, paths, expected):
        before = paths[:]
        result = Solution().findDuplicate(paths)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(group) is list and len(group) >= 2 for group in result))
        flattened = [path for group in result for path in group]
        self.assertTrue(all(type(path) is str for path in flattened))
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual(normalized(result), normalized(expected))
        self.assertEqual(paths, before)

    def test_all_small_content_assignments_and_three_layouts_against_original_records(self):
        cases = 0
        for size in range(1, 7):
            for contents in product(('a', 'A', 'ab', 'a1'), repeat=size):
                for layout in range(3):
                    paths, records = fixture(contents, layout)
                    self.check(paths, pairwise_content_groups(records))
                    cases += 1
        self.assertEqual(cases, 16380)

    def test_twenty_thousand_directories_long_lines_punctuation_and_sample(self):
        paths = [f'root/d{index} f.txt(' + ('a' if index % 2 == 0 else 'b') + ')' for index in range(20000)]
        self.assertLessEqual(sum(map(len, paths)), 500000)
        expected = [[f'root/d{index}/f.txt' for index in range(parity, 20000, 2)] for parity in range(2)]
        self.check(paths, expected)
        payload = 'x' * (3000 - len('root/a f.txt()'))
        lines = ['root/a f.txt(' + payload + ')', 'root/b f.txt(' + payload + ')']
        self.assertEqual(list(map(len, lines)), [3000, 3000])
        self.check(lines, [['root/a/f.txt', 'root/b/f.txt']])
        self.check(['root same.txt(a.b/1) unique.txt(q)', 'root/d same.txt(a.b/1) other.txt(a.b/2)'],
                   [['root/same.txt', 'root/d/same.txt']])
        self.check(['root/a f.txt(x(y))', 'root/b g.txt(x(y))'], [['root/a/f.txt', 'root/b/g.txt']])
        self.check(['root/a 1.txt(abcd) 2.txt(efgh)', 'root/c 3.txt(abcd)',
                    'root/c/d 4.txt(efgh)', 'root 4.txt(efgh)'],
                   [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']])


if __name__ == '__main__':
    unittest.main()
