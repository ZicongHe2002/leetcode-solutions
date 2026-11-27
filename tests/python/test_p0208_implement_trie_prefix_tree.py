import unittest
from itertools import product

from python.p0208_implement_trie_prefix_tree import Trie


class PrefixTrieTests(unittest.TestCase):
    def test_all_short_operation_programs_against_string_set(self):
        actions = [(operation, word) for operation in ('insert', 'search', 'startsWith') for word in ('a', 'ab', 'b')]
        programs = 0
        for size in range(5):
            for operations in product(actions, repeat=size):
                trie, words = Trie(), set()
                for operation, word in operations:
                    if operation == 'insert':
                        self.assertIsNone(trie.insert(word))
                        words.add(word)
                    else:
                        result = trie.search(word) if operation == 'search' else trie.startsWith(word)
                        expected = word in words if operation == 'search' else any(value.startswith(word) for value in words)
                        self.assertIs(type(result), bool)
                        self.assertEqual(result, expected)
                programs += 1
        self.assertEqual(programs, 7381)

    def test_maximum_calls_word_length_and_prefix_terminal_distinction(self):
        trie = Trie()
        longest = 'a' * 2000
        self.assertIsNone(trie.insert(longest))
        self.assertTrue(trie.search(longest))
        self.assertFalse(trie.search(longest[:-1]))
        self.assertTrue(trie.startsWith(longest[:-1]))
        for index in range(9998):
            suffix = ''.join(chr(ord('a') + index // 26**place % 26) for place in (2, 1, 0))
            word = 'k' + suffix
            self.assertIsNone(trie.insert(word))
            self.assertTrue(trie.search(word))
            self.assertTrue(trie.startsWith(word[:2]))
        self.assertFalse(trie.search('b' * 2000))
        self.assertFalse(trie.startsWith('b' * 2000))


if __name__ == '__main__':
    unittest.main()
