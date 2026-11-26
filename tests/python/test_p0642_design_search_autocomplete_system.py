import random
import unittest

from python.p0642_design_search_autocomplete_system import AutocompleteSystem


class FullScanOracle:
    def __init__(self, sentences, times):
        self.counts = {}
        for sentence, count in zip(sentences, times):
            self.counts[sentence] = self.counts.get(sentence, 0) + count
        self.prefix = ''

    def input(self, char):
        if char == '#':
            self.counts[self.prefix] = self.counts.get(self.prefix, 0) + 1
            self.prefix = ''
            return []
        self.prefix += char
        matching = [sentence for sentence in self.counts if sentence.startswith(self.prefix)]
        return sorted(matching, key=lambda item: (-self.counts[item], item))[:3]


class AutocompleteTests(unittest.TestCase):
    def test_hundred_systems_with_fifty_complete_sentences_against_full_scan(self):
        rng = random.Random(642)
        pool = ['a', 'ab', 'a b', 'ba', 'b a', 'b', 'aa', 'a a', 'cab']
        for _ in range(100):
            sentences = rng.sample(pool, rng.randint(1, len(pool)))
            times = [rng.randint(1, 50) for _ in sentences]
            before = sentences[:], times[:]
            actual, oracle = AutocompleteSystem(sentences, times), FullScanOracle(sentences, times)
            calls = 0
            for _ in range(50):
                text = rng.choice(pool + ['c', 'c a', 'cc'])
                for char in text + '#':
                    result = actual.input(char)
                    self.assertIs(type(result), list)
                    self.assertEqual(result, oracle.input(char))
                    calls += 1
            self.assertLessEqual(calls, 5000)
            self.assertEqual((sentences, times), before)

    def test_frequency_updates_ascii_space_order_and_return_copy(self):
        system = AutocompleteSystem(['i love you', 'island', 'iroman', 'i love leetcode'], [5, 3, 2, 2])
        self.assertEqual(system.input('i'), ['i love you', 'island', 'i love leetcode'])
        self.assertEqual(system.input(' '), ['i love you', 'i love leetcode'])
        self.assertEqual(system.input('a'), [])
        self.assertEqual(system.input('#'), [])
        for _ in range(2):
            for char in 'i a#':
                system.input(char)
        self.assertEqual(system.input('i'), ['i love you', 'i a', 'island'])
        other = AutocompleteSystem(['a', 'aa', 'ab', 'ac'], [5, 4, 3, 2])
        returned = other.input('a')
        returned[0] = 'modified'
        self.assertEqual(other.input('a'), ['aa'])
        self.assertEqual(other.input('#'), [])
        self.assertEqual(other.input('a'), ['a', 'aa', 'ab'])

    def test_maximum_history_and_exactly_five_thousand_inputs(self):
        sentences = ['a' * 98 + chr(97 + index // 10) + chr(97 + index % 10)
                     for index in range(100)]
        times = [index % 50 + 1 for index in range(100)]
        before = sentences[:], times[:]
        actual, oracle = AutocompleteSystem(sentences, times), FullScanOracle(sentences, times)
        stream = ('z' * 199 + '#') * 25
        self.assertEqual(len(stream), 5000)
        for char in stream:
            self.assertEqual(actual.input(char), oracle.input(char))
        self.assertEqual((sentences, times), before)


if __name__ == '__main__':
    unittest.main()
