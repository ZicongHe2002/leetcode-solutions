import re
import unittest
from itertools import product

from python.p0722_remove_comments import Solution


COMMENT = re.compile(r'//[^\n]*|/\*[\s\S]*?\*/|/\*')


def whole_program_regex(source):
    program = '\n'.join(source)
    matches = list(COMMENT.finditer(program))
    if any(match.group() == '/*' for match in matches):
        return None
    return [line for line in COMMENT.sub('', program).split('\n') if line]


class RemoveCommentsTests(unittest.TestCase):
    def check(self, source, expected=None):
        before = source[:]
        result = Solution().removeComments(source)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(line) is str and line for line in result))
        self.assertEqual(result, whole_program_regex(source) if expected is None else expected, source)
        self.assertEqual(source, before)

    def test_every_short_legal_program_against_whole_text_regex(self):
        legal = 0
        for size in range(9):
            for chars in product('a/*\n', repeat=size):
                source = ''.join(chars).split('\n')
                expected = whole_program_regex(source)
                if expected is not None:
                    self.check(source, expected)
                    legal += 1
        self.assertGreater(legal, 50000)

    def test_examples_nonoverlapping_delimiters_whitespace_and_full_source_boundary(self):
        self.check(['/*Test program */', 'int main()', '{ ', '  // variable declaration ',
                    'int a, b, c;', '/* This is a test', '   multiline  ', '   comment for ',
                    '   testing */', 'a = b + c;', '}'],
                   ['int main()', '{ ', '  ', 'int a, b, c;', 'a = b + c;', '}'])
        self.check(['a/*comment', 'line', 'more_comment*/b'], ['ab'])
        self.check(['a/*/', 'x*/b'], ['ab'])
        self.check(['a// /*', 'b/**/c', '', '   ', '/'], ['a', 'bc', '   ', '/'])
        self.check(['//*', 'x'], ['x'])
        self.check(['//* /', 'a/*//*/b'], ['ab'])
        self.check(['*' + '/**/' + '/x'], ['*/x'])
        source = ['x' * 78 + '/*'] + ['/' * 80] * 98 + ['*/' + 'y' * 78]
        self.assertEqual((len(source), {len(line) for line in source}), (100, {80}))
        self.check(source, ['x' * 78 + 'y' * 78])
        self.check([''] * 100, [])


if __name__ == '__main__':
    unittest.main()
