from itertools import product
import unittest

from python.p0331_verify_preorder_serialization_of_a_binary_tree import Solution


def recursive_tree_grammar_oracle(text):
    tokens = text.split(',')

    def consume(index):
        if index == len(tokens):
            raise ValueError('missing child')
        if tokens[index] == '#':
            return index + 1
        after_left = consume(index + 1)
        return consume(after_left)

    try:
        return consume(0) == len(tokens)
    except ValueError:
        return False


class SerializationSlotGrammarTests(unittest.TestCase):
    def test_all_small_well_formed_tokens_against_recursive_tree_grammar(self):
        streams = 0
        for size in range(1, 11):
            for tokens in product(('9', '#'), repeat=size):
                text = ','.join(tokens)
                actual = Solution().isValidSerialization(text)
                self.assertIs(type(actual), bool)
                self.assertEqual(actual, recursive_tree_grammar_oracle(text))
                streams += 1
        self.assertEqual(streams, 2046)

    def test_multidigit_nodes_prefix_exhaustion_and_maximum_text_length(self):
        for text, expected in [('#', True), ('100,#,#', True), ('9,#,92,#,#', True), ('9,#', False), ('#,#,9', False), ('9,#,#,#', False), ('', False)]:
            self.assertEqual(Solution().isValidSerialization(text), expected)
        text = ','.join(['10'] * 3 + ['1'] * 2496 + ['#'] * 2500)
        self.assertEqual(len(text), 10000)
        self.assertTrue(Solution().isValidSerialization(text))
        self.assertFalse(Solution().isValidSerialization(text[:-2]))


if __name__ == '__main__':
    unittest.main()
