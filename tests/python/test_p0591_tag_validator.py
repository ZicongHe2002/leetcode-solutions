from itertools import product
import re
import unittest

from python.p0591_tag_validator import Solution


TOKEN = re.compile(r'<!\[CDATA\[.*?\]\]>|</?[A-Z]{1,9}>|[^<]+', re.DOTALL)
OPENING = re.compile(r'<[A-Z]{1,9}>')


def grammar_oracle(code):
    tokens, consumed = [], 0
    for match in TOKEN.finditer(code):
        if match.start() != consumed:
            return False
        tokens.append(match.group())
        consumed = match.end()
    if consumed != len(code):
        return False

    def element(index):
        if index >= len(tokens) or OPENING.fullmatch(tokens[index]) is None:
            raise ValueError('An element starts with a valid opening tag')
        name = tokens[index][1:-1]
        index += 1
        while index < len(tokens):
            token = tokens[index]
            if token.startswith('</'):
                if token != '</' + name + '>':
                    raise ValueError('Mismatched closing element')
                return index + 1
            if token.startswith('<![CDATA[') or not token.startswith('<'):
                index += 1
            else:
                index = element(index)
        raise ValueError('Unclosed element')

    try:
        return element(0) == len(tokens)
    except ValueError:
        return False


class TagValidatorTests(unittest.TestCase):
    def check(self, code, expected):
        result = Solution().isValid(code)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected, code)

    def test_exhaustive_short_strings_and_generated_grammar_deletions(self):
        checks = 0
        for size in range(8):
            for letters in product('<>/Ax', repeat=size):
                code = ''.join(letters)
                self.check(code, grammar_oracle(code))
                checks += 1
        self.assertEqual(checks, 97656)
        names = ('A', 'ABC', 'ABCDEFGHI')
        texts = ('', 'x', '>', ']]>', ' / ![]', '<![CDATA[<a></B>]]>', '<![CDATA[]]>')
        basic = ['<' + name + '>' + text + '</' + name + '>' for name in names for text in texts]
        generated = set(basic)
        for name in names:
            for child in basic:
                for content in (child, 'x' + child, child + 'x', child + child):
                    generated.add('<' + name + '>' + content + '</' + name + '>')
        self.assertEqual(len(generated), 273)
        for code in generated:
            self.assertTrue(grammar_oracle(code))
            self.check(code, True)
            for index in range(len(code)):
                changed = code[:index] + code[index + 1:]
                self.check(changed, grammar_oracle(changed))

    def test_cdata_first_terminator_root_names_and_maximum_length(self):
        cases = (
            ('<A><![CDATA[</A>]]></A>', True),
            ('<A><![CDATA[one]]>two]]></A>', True),
            ('<A><![CDATA[<![CDATA[<x>]]></A>', True),
            ('<A>]]></A>', True),
            ('<![CDATA[<A></A>]]>', False),
            ('<A><![CDATA[<B>]]></B></A>', False),
            ('<A><![CDATA[x</A>', False),
            ('<A></A><B></B>', False),
            (' <A></A>', False),
            ('<A></A> ', False),
            ('<A><B></A></B>', False),
            ('<A/>', False),
            ('<ABCDEFGHI></ABCDEFGHI>', True),
            ('<ABCDEFGHIJ></ABCDEFGHIJ>', False),
        )
        for code, expected in cases:
            self.check(code, expected)
            self.assertEqual(grammar_oracle(code), expected)
        code = '<A>' + 'x' * 493 + '</A>'
        self.assertEqual(len(code), 500)
        self.check(code, True)
        nested = '<A>' * 71 + '</A>' * 71
        self.assertEqual(len(nested), 497)
        self.check(nested, True)
        self.check('<A>' * 71 + '</A>' * 70 + '</B>', False)


if __name__ == '__main__':
    unittest.main()
